import sys
import os
import glob
import re
import datetime
import pandas as pd
from collections import defaultdict
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

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
OUTPUT_PATH = r"C:\Users\Kandriad\Desktop\CoursePercentages.xlsx"

special_forms = ["1_ml", "0.5_ml", "1_ul"]

# Categories where Notes should NOT split items into separate rows — all
# notes variants collapse into a single row per item, and the Notes column
# is dropped from that category's sheet. Category names must match exactly
# what's in your Category dropdown.
CATEGORIES_WITHOUT_NOTES = set([
    "Antibiotics",
    "Biological",
    "Chemical",
    "Supply",
])

# Category that should use the SAME notes handling as the TOTAL Media sheet
# (only additive/pH info kept, via extract_relevant_notes) instead of full
# notes text or no notes at all.
CATEGORY_USES_MEDIA_NOTES_RULE = "Uninoculated Media"

# ============================================
# Library synonym resolution (same lookup pattern as the cost-analysis script)
# ============================================
LIBRARY_MAP = {
    "Biological": bacteria.bacteria_list,
    "Uninoculated Media": media.media_list,
    "Chemical": chemicals.chemical_list,
    "Supply": supplies.supplies,
    "Antibiotics": antibiotics.antibiotics,
}

_unmatched_names = set()  # (category, raw_name) pairs we couldn't resolve — reported at the end

def resolve_canonical_name(name, category):
    """
    Look up `name` in the library dict for `category` by key, by its "name"
    field, or by any listed synonym — same three-way match the cost script
    uses. Returns the library's canonical "name" (falling back to the dict
    key, then to the original string) so that e.g. "E. coli" and "E.coli"
    collapse into a single row when grouping.
    """
    if not name or str(name).strip().lower() == "nan":
        return ""
    name_clean = str(name).strip()
    name_lower = name_clean.lower()

    library_dict = LIBRARY_MAP.get(category)
    if not library_dict:
        return name_clean  # no library for this category (shouldn't normally happen)

    for key, info in library_dict.items():
        if key.strip().lower() == name_lower:
            return str(info.get("name", key)).strip()
        if str(info.get("name", "")).strip().lower() == name_lower:
            return str(info.get("name", key)).strip()
        synonyms = info.get("synonyms") or info.get("synonym")
        if synonyms:
            if isinstance(synonyms, str):
                synonyms = [synonyms]
            if any(str(s).strip().lower() == name_lower for s in synonyms):
                return str(info.get("name", key)).strip()

    _unmatched_names.add((category, name_clean))
    return name_clean  # not found in library — keep original so nothing silently vanishes

# ============================================
# Utility functions (shared logic, pulled from the media-needs script)
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
    """Only keep additive or pH info from experiment notes. Used only for the
    Media grouping key, so it matches the same collapsing rules the media
    needs report uses (e.g. '5% sheep blood, keep at 4C' and '5%blood' should
    end up as the same media key)."""
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

def parse_week_string(week_value):
    """More robust version (handles real datetime/Timestamp values, not just
    strings) — pulled from the prep-list script."""
    if pd.isna(week_value):
        return datetime.datetime.max
    if isinstance(week_value, pd.Timestamp):
        return week_value.to_pydatetime()
    if isinstance(week_value, (datetime.datetime, datetime.date)):
        return datetime.datetime.combine(week_value, datetime.datetime.min.time())

    week_str = str(week_value).strip()
    if not week_str:
        return datetime.datetime.max

    week_str = week_str.replace("Sept", "Sep").replace("–", "-").replace("—", "-")
    week_str = re.sub(r'([A-Za-z]+)(\d)', r'\1 \2', week_str)

    try:
        first_part = week_str.split("-")[0].strip()
        current_year = datetime.datetime.now().year
        return datetime.datetime.strptime(f"{first_part} {current_year}", "%b %d %Y")
    except Exception:
        return datetime.datetime.max

def extract_course_from_filename(filepath):
    """'140LExperiments.xlsx' -> '140'. Falls back to the base filename
    (minus 'Experiments') if no leading digits are found."""
    base = os.path.splitext(os.path.basename(filepath))[0]
    base = re.sub(r"Experiments$", "", base, flags=re.IGNORECASE)
    match = re.match(r"^(\d+)", base)
    if match:
        return match.group(1)
    return base if base else "Unknown"

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

def parse_sheet_with_header_search(xls, sheet_name, search_col):
    """Find the row that actually contains search_col as a header, then
    re-read with that row as the header. Falls back to row 0."""
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

def course_sort_key(course):
    return (0, int(course)) if course.isdigit() else (1, course)

# ============================================
# SINGLE-PASS READ: every experiment file/sheet read from disk exactly once
# ============================================
def build_all_items():
    """
    Reads every *Experiments.xlsx file and every sheet it references ONE
    time each. Unlike the media-needs script, this does NOT filter against
    MediaInventory.xlsx — we want every item (bacteria, media, supplies,
    antibiotics, chemicals) regardless of whether it's tracked in inventory.

    Each returned dict carries both the Item/Organism name AND the Media
    Used/Form for that same row, so a Biological entry contributes its
    quantity to both its bacteria bucket and its media bucket downstream.
    """
    pattern = os.path.join(EXPFILES_PATH, "*Experiments.xlsx")
    experiment_files = glob.glob(pattern)

    all_items = []

    print(f"⏳ Reading {len(experiment_files)} experiment file(s) from disk (single pass)...")
    for file_idx, file in enumerate(experiment_files, start=1):
        print(f"   [{file_idx}/{len(experiment_files)}] parsing: {os.path.basename(file)}")

        course_name = extract_course_from_filename(file)

        xls = pd.ExcelFile(file)
        course_df = parse_sheet_with_header_search(xls, "CourseInfo", "Students")
        course_info = load_course_info(course_df)
        schedule_df = parse_sheet_with_header_search(xls, "ExperimentIndex", "Week")

        sheet_cache = {}

        for _, row in schedule_df.iterrows():
            week = row["Week"]
            if pd.isna(week):
                continue

            sheet_name = str(row["SheetName"])
            if sheet_name.endswith(".0"):
                sheet_name = sheet_name[:-2]
            sheet_name = sheet_name.strip()

            if sheet_name not in xls.sheet_names:
                print(f"   Missing sheet: {sheet_name} in {os.path.basename(file)}")
                continue

            if sheet_name not in sheet_cache:
                sheet_cache[sheet_name] = parse_sheet_with_header_search(xls, sheet_name, "Category")
            exp_df = sheet_cache[sheet_name]

            for _, entry in exp_df.iterrows():
                category = str(entry.get("Category", "")).strip()
                if not category or category.lower() == "nan":
                    continue

                # Item name: Item/Organism, or fall back to Media Used for
                # Uninoculated Media rows (same rule as the prep-list script)
                item_name_raw = entry.get("Item/Organism")
                if (item_name_raw is None or pd.isna(item_name_raw) or str(item_name_raw).strip() == "") \
                        and category.strip().lower() == "uninoculated media":
                    item_name_raw = entry.get("Media Used")
                item_name_raw = str(item_name_raw).strip() if item_name_raw is not None and not pd.isna(item_name_raw) else ""

                media_used_raw = entry.get("Media Used")
                media_used_raw = str(media_used_raw).strip() if media_used_raw is not None and not pd.isna(media_used_raw) else ""

                # Canonicalize through the libraries so synonyms collapse
                # together instead of splitting a course's percentage across
                # multiple spellings of the same item.
                media_used = resolve_canonical_name(media_used_raw, "Uninoculated Media") if media_used_raw else ""
                item_name = resolve_canonical_name(item_name_raw, category) if item_name_raw else ""

                form_raw = entry.get("Form")
                form = str(form_raw).strip().replace(" ", "_") if form_raw is not None and not pd.isna(form_raw) else ""

                raw_notes = entry.get("Notes")
                media_notes_key = normalize_notes(extract_relevant_notes(raw_notes))

                # Item-level notes key has three possible rules:
                #  1. Categories in CATEGORIES_WITHOUT_NOTES -> always blank
                #  2. Uninoculated Media -> same "relevant notes only" rule
                #     as the TOTAL Media sheet (reuses media_notes_key)
                #  3. Everything else -> full normalized notes
                if category in CATEGORIES_WITHOUT_NOTES:
                    item_notes_key = ""
                elif category == CATEGORY_USES_MEDIA_NOTES_RULE:
                    item_notes_key = media_notes_key
                else:
                    item_notes_key = normalize_notes(raw_notes)

                if form in special_forms:
                    quantity = entry.get("Volume", 0)
                else:
                    quantity = entry.get("Quantity", 0)
                dist_type = str(entry.get("DistributionType", "")).strip().title()

                try:
                    total_qty = calculate_total_qty(quantity, dist_type, course_info, form)
                except Exception as e:
                    print(f"   Error calculating qty for {course_name} {category} {item_name}: {e}")
                    continue

                if pd.isna(total_qty):
                    continue

                all_items.append({
                    "Course": course_name,
                    "Sheet": sheet_name,
                    "Category": category,
                    "Item": item_name,
                    "Media Used": media_used,
                    "Form": form,
                    "ItemNotes": item_notes_key,
                    "MediaNotes": media_notes_key,
                    "Total Quantity": float(total_qty)
                })

    print("✅ Finished single-pass read of all experiment files.")

    missing_form = [i for i in all_items if i["Media Used"] and not i["Form"]]
    if missing_form:
        print(f"\n⚠ {len(missing_form)} row(s) have a Media Used value but NO Form — "
              f"these were previously silently dropped by the media-needs script "
              f"(they never matched an inventory key) and are likely caused by "
              f"merged 'Form' cells in the source sheet. Check these:")
        seen = set()
        for i in missing_form:
            trace = (i["Course"], i["Sheet"], i["Media Used"])
            if trace in seen:
                continue
            seen.add(trace)
            print(f"   Course '{i['Course']}', Sheet '{i['Sheet']}': Media Used = '{i['Media Used']}'")
        print()

    if _unmatched_names:
        print(f"\n⚠ {len(_unmatched_names)} name(s) not found in any library (kept as-typed):")
        for cat, name in sorted(_unmatched_names):
            print(f"   [{cat}] {name}")
        print()

    return all_items

# ============================================
# Aggregation
# ============================================
def build_media_usage_by_course(all_items):
    """
    Keyed by (Media Used, Form, Notes) -> {course: qty}.
    Includes every row that has a Media Used value, REGARDLESS of Category —
    this is what pulls biological-growth media into the media totals.
    """
    usage = defaultdict(lambda: defaultdict(float))
    for item in all_items:
        if not item["Media Used"]:
            continue
        key = (item["Media Used"], item["Form"], item["MediaNotes"])
        usage[key][item["Course"]] += item["Total Quantity"]
    return usage

def build_item_usage_by_course(all_items):
    """
    Keyed by (Category, Item, Form, Notes) -> {course: qty}.
    Covers bacteria (Biological), supplies, antibiotics, chemicals, etc.
    Same Total Quantity value used here as in the media bucket above — it's
    the same physical row, just grouped a second way.

    Form is only meaningful for Uninoculated Media (plate vs. broth vs.
    slant of the same media should be separate rows) — it's forced blank
    for every other category so those sheets stay grouped the same way
    they always were.
    """
    usage = defaultdict(lambda: defaultdict(float))
    for item in all_items:
        if not item["Item"]:
            continue
        form_key = item["Form"] if item["Category"] == CATEGORY_USES_MEDIA_NOTES_RULE else ""
        key = (item["Category"], item["Item"], form_key, item["ItemNotes"])
        usage[key][item["Course"]] += item["Total Quantity"]
    return usage

# ============================================
# Excel export (styling matches the media-needs export)
# ============================================
def write_percentage_sheet(wb, sheet_title, rows, label_headers, all_courses, sheet_index=None):
    """
    rows: list of dicts, each with keys matching label_headers, plus
          "Total Need" and "Course Pcts" ({course: pct 0-100})
    """
    if sheet_index == 0:
        ws = wb.active
        ws.title = sheet_title
    else:
        ws = wb.create_sheet(title=sheet_title)

    header_font  = Font(name="Consolas", bold=True, color="FFFFFF", size=12)
    header_fill  = PatternFill("solid", start_color="4D4D4D")
    data_font    = Font(name="Consolas", size=11)
    alt_fill     = PatternFill("solid", start_color="B2B2B2")
    center_align = Alignment(horizontal="center", vertical="center")
    left_align   = Alignment(horizontal="left", vertical="center")

    base_widths = {"Category": 16, "Item": 30, "Media Used": 30, "Form": 18, "Notes": 28, "Total Need": 14}
    course_headers = [f"{c} %" for c in all_courses]

    headers = label_headers + ["Total Need"] + course_headers
    col_widths = [base_widths.get(h, 20) for h in label_headers] + [14] + [12] * len(all_courses)

    for col_idx, (header, width) in enumerate(zip(headers, col_widths), start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        ws.column_dimensions[cell.column_letter].width = width
    ws.row_dimensions[1].height = 20

    num_base_cols = len(label_headers) + 1  # + Total Need

    for row_idx, row in enumerate(rows, start=2):
        fill = alt_fill if row_idx % 2 == 0 else PatternFill()
        values = [row[h] for h in label_headers] + [row["Total Need"]]
        values += [row["Course Pcts"].get(c, 0.0) for c in all_courses]

        for col_idx, value in enumerate(values, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.font = data_font
            cell.fill = fill
            if col_idx > num_base_cols:  # course % columns
                cell.alignment = center_align
                cell.number_format = '0.0"%"'
            elif headers[col_idx - 1] == "Total Need":
                cell.alignment = center_align
                cell.number_format = "#,##0"
            elif headers[col_idx - 1] in ("Form",):
                cell.alignment = center_align
            else:
                cell.alignment = left_align

    ws.freeze_panes = ws.cell(row=2, column=num_base_cols + 1).coordinate

def usage_dict_to_rows(usage_by_course, all_courses, key_labels):
    """Turn a {key_tuple: {course: qty}} dict into row dicts for export,
    computing per-course percentages of each item's own total."""
    rows = []
    for key, course_map in usage_by_course.items():
        total_need = sum(course_map.values())
        course_pcts = {
            c: (course_map.get(c, 0.0) / total_need * 100 if total_need > 0 else 0.0)
            for c in all_courses
        }
        row = dict(zip(key_labels, key))
        row["Total Need"] = total_need
        row["Course Pcts"] = course_pcts
        rows.append(row)
    rows.sort(key=lambda r: tuple(r[l] for l in key_labels))
    return rows

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    all_items = build_all_items()
    print(f"✅ Parsed {len(all_items)} total item rows across all experiment files")

    all_courses = sorted({i["Course"] for i in all_items}, key=course_sort_key)
    print(f"✅ Courses found: {all_courses}")

    # ---- Media usage (all categories combined, including biologicals) ----
    media_usage = build_media_usage_by_course(all_items)
    media_rows = usage_dict_to_rows(media_usage, all_courses, ["Media Used", "Form", "Notes"])

    # ---- Item usage, split into a sheet per Category (bacteria, supplies, etc.) ----
    item_usage = build_item_usage_by_course(all_items)
    item_rows = usage_dict_to_rows(item_usage, all_courses, ["Category", "Item", "Notes"])

    categories = sorted({r["Category"] for r in item_rows})

    wb = Workbook()

    # Named "TOTAL Media" (not just "Media") since this combines media use
    # from every category, including media consumed to grow biologicals —
    # it will overlap with the separate "Uninoculated Media" category sheet,
    # so the name is meant to make that overlap obvious rather than confusing.
    write_percentage_sheet(
        wb, "TOTAL Media % by Course", media_rows,
        label_headers=["Media Used", "Form", "Notes"],
        all_courses=all_courses, sheet_index=0
    )

    for idx, cat in enumerate(categories, start=1):
        # Build fresh copies (without "Category", which is redundant within
        # its own sheet) rather than mutating the shared row dicts in
        # item_rows — mutating in place would corrupt rows still waiting to
        # be filtered on later loop iterations.
        drop_notes = cat in CATEGORIES_WITHOUT_NOTES
        drop_keys = {"Category", "Notes"} if drop_notes else {"Category"}
        cat_rows = [
            {k: v for k, v in r.items() if k not in drop_keys}
            for r in item_rows if r["Category"] == cat
        ]
        safe_title = cat[:31] if cat else f"Category{idx}"
        write_percentage_sheet(
            wb, safe_title, cat_rows,
            label_headers=["Item"] if drop_notes else ["Item", "Notes"],
            all_courses=all_courses, sheet_index=idx
        )

    wb.save(OUTPUT_PATH)
    print(f"✅ Course percentages exported to: {OUTPUT_PATH}")