import sys
import os
import glob
import re
import datetime
import pandas as pd
from collections import defaultdict
import warnings
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# ============================================
# Path setup
# ============================================
script_dir = os.path.dirname(os.path.abspath(__file__))
libraries_path = os.path.join(script_dir, "..", "Libraries")
if libraries_path not in sys.path:
    sys.path.append(libraries_path)

import bacteria
import media
import supplies
import antibiotics
import chemicals

# ============================================
# Constants
# ============================================
EXPFILES_PATH = r"C:\Users\Kandriad\Desktop\ExpFiles"
INVENTORY_PATH = r"C:\Users\Kandriad\Desktop\MediaInventory.xlsx"  # pulls counts of what have
MEDIA_NEEDS_OUTPUT = r"C:\Users\Kandriad\Desktop\F26Media_Needs.xlsx"

special_forms = ["1_ml", "0.5_ml", "1_ul"]

# ============================================
# Utility functions
# ============================================
def normalize_notes(notes):
    if not isinstance(notes, str):
        return ""
    notes = notes.lower().strip()
    notes = re.sub(r"\s+", " ", notes)
    notes = notes.replace("with ", "w/")
    notes = notes.replace(" w/ ", " w/")
    return notes

def extract_relevant_notes(notes):
    """Only keep additive or pH info from experiment notes."""
    if not isinstance(notes, str):
        return ""
    notes = notes.lower()
    additive_match = re.search(r"(w/\S+)", notes)
    ph_match = re.search(r"(ph\d+)", notes)
    parts = []
    if additive_match:
        parts.append(additive_match.group(1))
    if ph_match:
        parts.append(ph_match.group(1))
    return " ".join(parts)

def parse_week_string(week_str):
    if not isinstance(week_str, str) or not week_str.strip():
        return datetime.datetime.max
    week_str = week_str.replace("Sept", "Sep")
    week_str = re.sub(r'([A-Za-z]+)(\d)', r'\1 \2', week_str)
    try:
        first_part = week_str.split("-")[0].strip()
        return datetime.datetime.strptime(first_part + " 2025", "%b %d %Y")
    except Exception:
        return datetime.datetime.max

def load_course_info(course_df):
    row = course_df.iloc[0]
    return {
        "students": int(row["Students"]),
        "sections": int(row["Sections"]),
        "groups":   int(row["Groups"]),
        "rooms":    row["Rooms"].split(", ")
    }

def calculate_total_qty(quantity, dist_type, course_info, form=None):
    multiplier = {
        "Per Student": course_info["students"],
        "Per Pair": course_info["students"] // 2,
        "Per Group": course_info["groups"],
        "Per Table": sum(5 if room.strip() == "113" else 6 for room in course_info["rooms"]),
        "Per Section": course_info["sections"],
        "Per Room": len(course_info["rooms"]),
        "Per Course": 1
    }.get(dist_type, 1)
    if form in special_forms:
        return multiplier
    else:
        return quantity * multiplier

# ============================================
# Inventory loading
# ============================================
def load_media_inventory(INVENTORY_PATH):
    df = pd.read_excel(INVENTORY_PATH, sheet_name="Inventory", header=0)
    inventory = {}
    for _, row in df.iterrows():
        key = (
            str(row["Media Used"]).strip(),
            str(row["Form"]).strip().replace(" ", "_"),
            normalize_notes(row["Notes"])
        )
        inventory[key] = float(row["HAVE"])
    return inventory

# ============================================
# Experiment parsing
# ============================================
def parse_sheet_with_header_search(xls, sheet_name, search_col):
    """
    Parse a sheet by first searching for the row that contains search_col
    as a header, then re-reading with that row as the header.
    Falls back to row 0 if the column is not found.
    """
    raw_df = xls.parse(sheet_name, header=None)
    header_row = None
    for i, row in raw_df.iterrows():
        if search_col in [str(v).strip() for v in row.values]:
            header_row = i
            break
    if header_row is None:
        print(f"Warning: could not find '{search_col}' header in sheet '{sheet_name}', defaulting to row 0")
        header_row = 0
    df = xls.parse(sheet_name, header=header_row)
    df.columns = df.columns.str.strip()
    return df

# ============================================
# SINGLE-PASS CACHE BUILDER
# ============================================
# This replaces the old pattern of re-opening and re-parsing every Excel
# file from disk once per week, per call site (it was happening 3x total
# across the script). Instead, every file and every sheet is read from
# disk exactly ONCE here, and everything downstream just looks things up
# from the in-memory cache below.

def build_weekly_items_cache(inventory_keys):
    """
    Reads every *Experiments.xlsx file and every sheet it references ONE
    time each, and returns a dict: {week_number: [list of item dicts]}
    """
    pattern = os.path.join(EXPFILES_PATH, "*Experiments.xlsx")
    experiment_files = glob.glob(pattern)

    weekly_items_cache = defaultdict(list)

    print(f"⏳ Reading {len(experiment_files)} experiment file(s) from disk (single pass)...")
    for file_idx, file in enumerate(experiment_files, start=1):
        print(f"   [{file_idx}/{len(experiment_files)}] parsing: {os.path.basename(file)}")

        xls = pd.ExcelFile(file)
        course_df = parse_sheet_with_header_search(xls, "CourseInfo", "Students")
        course_info = load_course_info(course_df)
        schedule_df = parse_sheet_with_header_search(xls, "ExperimentIndex", "Week")

        # Cache each experiment sheet within this file so it's only parsed once,
        # even if it's referenced by multiple weeks/rows.
        sheet_cache = {}

        for _, row in schedule_df.iterrows():
            week = row["Week"]
            if pd.isna(week):
                continue

            sheet_name = str(row["SheetName"])
            if sheet_name.endswith(".0"):
                sheet_name = sheet_name[:-2]
            if sheet_name not in xls.sheet_names:
                continue

            if sheet_name not in sheet_cache:
                sheet_cache[sheet_name] = parse_sheet_with_header_search(xls, sheet_name, "Category")
            exp_df = sheet_cache[sheet_name]

            for _, entry in exp_df.iterrows():
                media_used = entry.get("Media Used")
                if not media_used or pd.isna(media_used) or str(media_used).strip() == "":
                    continue

                form_raw = entry.get("Form")
                form = str(form_raw).strip().replace(" ", "_") if form_raw else ""
                notes_key = normalize_notes(extract_relevant_notes(entry.get("Notes")))

                key = (str(media_used).strip(), form, notes_key)
                if key not in inventory_keys:
                    continue

                if form in special_forms:
                    quantity = entry.get("Volume", 0)
                else:
                    quantity = entry.get("Quantity", 0)
                dist_type = str(entry.get("DistributionType", "")).strip().title()
                try:
                    total_qty = calculate_total_qty(quantity, dist_type, course_info, form)
                except Exception:
                    continue

                weekly_items_cache[week].append({
                    "Media Used": media_used,
                    "Form": form,
                    "Total Quantity": float(total_qty),
                    "Notes": notes_key
                })

    print("✅ Finished single-pass read of all experiment files.")
    return weekly_items_cache

def get_all_weeks_from_cache(weekly_items_cache):
    return sorted(weekly_items_cache.keys(), key=lambda w: parse_week_string(str(w)))

# ============================================
# Inventory usage calculation
# ============================================
def calculate_media_usage(all_items):
    usage = defaultdict(float)
    for item in all_items:
        key = (item["Media Used"], item["Form"], item["Notes"])
        usage[key] += item["Total Quantity"]
    return usage

# ============================================
# Low stock thresholds
# ============================================
def get_low_stock_threshold(media_name, form, notes):
    media_name = media_name.lower()
    form = form.lower()
    notes = notes.lower()
    if "premade" in form:
        return 1
    elif "plate" in form:
        return 50
    else:
        return 72

# ============================================
# Week-by-week forecast
# ============================================
def forecast_weekly_inventory(inventory, all_weeks, weekly_items_cache):
    inv = inventory.copy()
    first_low_week = {}
    usage_schedule = defaultdict(list)

    print("⏳ Building usage schedule from cache...")
    for week in all_weeks:
        weekly_items = weekly_items_cache.get(week, [])
        for item in weekly_items:
            key = (item["Media Used"], item["Form"], normalize_notes(item["Notes"]))
            usage_schedule[key].append(week)

    for key, qty in inv.items():
        threshold = get_low_stock_threshold(*key)
        if qty < threshold and key not in first_low_week:
            next_usage = usage_schedule[key][0] if usage_schedule[key] else None
            first_low_week[key] = {
                "warning_week": "START OF SEMESTER",
                "remaining_before": qty,
                "next_low_week": next_usage
            }

    print("⏳ Simulating inventory drawdown week by week...")
    for week in all_weeks:
        weekly_items = weekly_items_cache.get(week, [])
        usage = calculate_media_usage(weekly_items)

        for key, qty_used in usage.items():
            if key not in inv:
                continue

            threshold = get_low_stock_threshold(*key)
            remaining_before = inv[key]
            remaining_after = remaining_before - qty_used
            inv[key] = remaining_after

            if remaining_before >= threshold and remaining_after < threshold and key not in first_low_week:
                future_weeks = [w for w in usage_schedule[key] if parse_week_string(str(w)) > parse_week_string(str(week))]
                next_usage = future_weeks[0] if future_weeks else None

                first_low_week[key] = {
                    "warning_week": week,
                    "remaining_before": remaining_before,
                    "next_low_week": next_usage
                }

    print("✅ Finished drawdown simulation.")
    return first_low_week, inv

# ============================================
# Export media needs to Excel ##NEED TO FIND A WAY TO HAVE IT PUT IN ALL MEDIA INCLUDING THOSE THAT ARE ZERO
# ============================================
def export_media_needs(all_weeks, weekly_items_cache, inventory, output_path=MEDIA_NEEDS_OUTPUT):
    # Gather and aggregate all needs across every week (from cache, no re-reading disk)
    all_items = []
    print("⏳ Aggregating totals for export...")
    for week in all_weeks:
        all_items.extend(weekly_items_cache.get(week, []))

    usage = calculate_media_usage(all_items)

    # Start from EVERY item in MediaInventory.xlsx (defaulting to 0 need),
    # then layer in any actual usage found. This guarantees items that were
    # never used this semester still show up in the export with 0.
    all_keys = set(inventory.keys()) | set(usage.keys())

    rows = sorted(
        [
            {
                "Media Used": media_used,
                "Form": form,
                "Notes": notes,
                "Total Need": usage.get((media_used, form, notes), 0.0)
            }
            for (media_used, form, notes) in all_keys
        ],
        key=lambda r: (r["Media Used"], r["Form"], r["Notes"])
    )

    wb = Workbook()
    ws = wb.active
    ws.title = "Media Needs"

    # Styles
    header_font     = Font(name="Consolas", bold=True, color="FFFFFF", size=12)
    header_fill     = PatternFill("solid", start_color="4D4D4D")   # dark gray
    data_font       = Font(name="Consolas", size=11)
    alt_fill        = PatternFill("solid", start_color="B2B2B2")   # light gray stripe
    center_align    = Alignment(horizontal="center", vertical="center")
    left_align      = Alignment(horizontal="left",   vertical="center")

    headers = ["Media Used", "Form", "Notes", "Total Need"]
    col_widths = [30, 18, 28, 14]

    # Write headers
    for col_idx, (header, width) in enumerate(zip(headers, col_widths), start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        ws.column_dimensions[cell.column_letter].width = width

    ws.row_dimensions[1].height = 20

    # Write data rows
    for row_idx, row in enumerate(rows, start=2):
        fill = alt_fill if row_idx % 2 == 0 else PatternFill()
        values = [row["Media Used"], row["Form"], row["Notes"], row["Total Need"]]
        for col_idx, value in enumerate(values, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = data_font
            cell.fill = fill
            cell.alignment = center_align if col_idx in (2, 4) else left_align
            if col_idx == 4:
                cell.number_format = "#,##0"

    # Freeze header row
    ws.freeze_panes = "A2"

    wb.save(output_path)
    print(f"✅ Media needs exported to: {output_path}")

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    inventory = load_media_inventory(INVENTORY_PATH)
    print(f"✅ Loaded inventory: {len(inventory)} items")

    # Single disk pass: read every experiment file/sheet exactly once
    weekly_items_cache = build_weekly_items_cache(inventory.keys())

    all_weeks = get_all_weeks_from_cache(weekly_items_cache)
    print(f"✅ Found {len(all_weeks)} weeks to process")

    first_low_week, final_inventory = forecast_weekly_inventory(inventory, all_weeks, weekly_items_cache)

    print("\n=== WEEKLY LOW STOCK FORECAST ===\n")
    if not first_low_week:
        print("✅ All media stocks are above threshold for all weeks.")
    else:
        for key, info in first_low_week.items():
            media_name, form, notes = key
            warning_week = info["warning_week"]
            remaining = info["remaining_before"]
            next_low_week = info["next_low_week"]

            warning_date = parse_week_string(str(warning_week)).strftime("%b %d, %Y")
            if next_low_week:
                low_date = parse_week_string(str(next_low_week)).strftime("%b %d, %Y")
                next_text = f", if do not make more, will not have enough on: {low_date}"
            else:
                next_text = " Not Needed Again This Semester"

            print(f"🚨 {media_name} ({form}, {notes or 'no notes'}) → {remaining:.2f} remaining as of {warning_date}{next_text}")

    print("\n=== FINAL INVENTORY AFTER ALL WEEKS ===\n")
    for key, remaining in final_inventory.items():
        media_name, form, notes = key
        print(f"{media_name} | {form} | {notes or 'no notes'} → {remaining:.2f}")

    # Export media needs summary to Excel
    export_media_needs(all_weeks, weekly_items_cache, inventory)