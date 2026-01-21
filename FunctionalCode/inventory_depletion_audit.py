import sys
import os
import glob
import re
import datetime
import pandas as pd
from collections import defaultdict
import warnings

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
INVENTORY_PATH = r"C:\Users\Kandriad\Desktop\Sp26 Needs.xlsx"

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
    return {
        "students": int(course_df.loc[0, "Students"]),
        "sections": int(course_df.loc[0, "Sections"]),
        "groups": int(course_df.loc[0, "Groups"]),
        "rooms": course_df.loc[0, "Rooms"].split(", ")
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
    df = pd.read_excel(INVENTORY_PATH, sheet_name="MediaSummary1.21.26")
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
def get_all_weeks():
    pattern = os.path.join(EXPFILES_PATH, "*Experiments.xlsx")
    experiment_files = glob.glob(pattern)
    all_weeks = set()
    for file in experiment_files:
        xls = pd.ExcelFile(file)
        schedule_df = xls.parse("ExperimentIndex")
        schedule_df.columns = schedule_df.columns.str.strip()
        all_weeks.update(schedule_df["Week"].dropna().unique())
    return sorted(all_weeks, key=parse_week_string)

def gather_weekly_needs(week_number, inventory_keys):
    pattern = os.path.join(EXPFILES_PATH, "*Experiments.xlsx")
    experiment_files = glob.glob(pattern)
    weekly_items = []
    for file in experiment_files:
        course_name = os.path.basename(file).replace("Experiments.xlsx", "").strip()
        xls = pd.ExcelFile(file)
        course_df = xls.parse("CourseInfo")
        course_info = load_course_info(course_df)
        schedule_df = xls.parse("ExperimentIndex")
        schedule_df.columns = schedule_df.columns.str.strip()
        week_exps = schedule_df[schedule_df["Week"] == week_number]

        for _, row in week_exps.iterrows():
            sheet_name = str(row["SheetName"])
            if sheet_name.endswith(".0"):
                sheet_name = sheet_name[:-2]
            if sheet_name not in xls.sheet_names:
                continue
            exp_df = xls.parse(sheet_name)
            exp_df.columns = exp_df.columns.str.strip()

            for _, entry in exp_df.iterrows():
                media_used = entry.get("Media Used")
                if not media_used or pd.isna(media_used) or str(media_used).strip() == "":
                    continue  # skip irrelevant

                form_raw = entry.get("Form")
                form = str(form_raw).strip().replace(" ", "_") if form_raw else ""
                notes_key = normalize_notes(extract_relevant_notes(entry.get("Notes")))

                key = (str(media_used).strip(), form, notes_key)
                if key not in inventory_keys:
                    continue  # skip items not in inventory

                if form in special_forms:
                    quantity = entry.get("Volume", 0)
                else:
                    quantity = entry.get("Quantity", 0)
                dist_type = str(entry.get("DistributionType", "")).strip().title()
                try:
                    total_qty = calculate_total_qty(quantity, dist_type, course_info, form)
                except Exception:
                    continue

                weekly_items.append({
                    "Media Used": media_used,
                    "Form": form,
                    "Total Quantity": float(total_qty),
                    "Notes": notes_key
                })
    return weekly_items

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
def forecast_weekly_inventory(inventory, all_weeks):
    """
    Simulate week-by-week inventory and return:
    - first_low_week: dict of first week each item drops below threshold (before going negative)
    - remaining_inventory: final remaining quantities after all weeks
    """
    inv = inventory.copy()
    first_low_week = {}
    usage_schedule = defaultdict(list)

    # Build a schedule of when each media is used
    for week in all_weeks:
        weekly_items = gather_weekly_needs(week, inventory.keys())
        for item in weekly_items:
            key = (item["Media Used"], item["Form"], normalize_notes(item["Notes"]))
            usage_schedule[key].append(week)

    # Simulate week-by-week depletion
    for week in all_weeks:
        weekly_items = gather_weekly_needs(week, inventory.keys())
        usage = calculate_media_usage(weekly_items)

        for key, qty_used in usage.items():
            if key not in inv:
                continue

            threshold = get_low_stock_threshold(*key)
            remaining_before = inv[key]
            remaining_after = remaining_before - qty_used
            inv[key] = remaining_after

            # Check if this week is the first week the stock will drop below threshold
            if remaining_before >= threshold and remaining_after < threshold and key not in first_low_week:
                # The week AFTER this warning week is when stock would go below threshold
                future_weeks = [w for w in usage_schedule[key] if parse_week_string(str(w)) > parse_week_string(str(week))]
                next_usage = future_weeks[0] if future_weeks else None

                first_low_week[key] = {
                    "warning_week": week,                # last safe week
                    "remaining_before": remaining_before,
                    "next_low_week": next_usage          # first week that would be below threshold
                }

    return first_low_week, inv

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    inventory = load_media_inventory(INVENTORY_PATH)
    all_weeks = get_all_weeks()
    first_low_week, final_inventory = forecast_weekly_inventory(inventory, all_weeks)

    print("\n=== WEEKLY LOW STOCK FORECAST ===\n")
    if not first_low_week:
        print("✅ All media stocks are above threshold for all weeks.")
    else:
        for key, info in first_low_week.items():
            media, form, notes = key
            warning_week = info["warning_week"]
            remaining = info["remaining_before"]
            next_low_week = info["next_low_week"]

            warning_date = parse_week_string(str(warning_week)).strftime("%b %d, %Y")
            if next_low_week:
                low_date = parse_week_string(str(next_low_week)).strftime("%b %d, %Y")
                next_text = f", if do not make more, will not have engough on: {low_date}"
            else:
                next_text = " Not Needed Again This Semester"

            print(f"🚨 {media} ({form}, {notes or 'no notes'}) → {remaining:.2f} remaining as of {warning_date}{next_text}")

    print("\n=== FINAL INVENTORY AFTER ALL WEEKS ===\n")
    for key, remaining in final_inventory.items():
        media, form, notes = key
        print(f"{media} | {form} | {notes or 'no notes'} → {remaining:.2f}")
