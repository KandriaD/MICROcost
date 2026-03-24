import sys
import pandas as pd
import glob
import os
from docx import Document
from docx.shared import Pt, RGBColor
from datetime import datetime

# ----------------------------
# Setup paths and imports
# ----------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
library_path = os.path.abspath(os.path.join(script_dir, '..', 'Libraries'))
if library_path not in sys.path:
    sys.path.append(library_path)

import bacteria
import media
import supplies
import antibiotics
import chemicals

special_forms = ["1_ml", "0.5_ml", "1_ul"]

# ----------------------------
# COURSE + EXPERIMENT LOADING
# ----------------------------
def load_course_info(course_df):
    return {
        "students": int(course_df.loc[0, "Students"]),
        "sections": int(course_df.loc[0, "Sections"]),
        "groups":   int(course_df.loc[0, "Groups"]),
        "rooms":    course_df.loc[0, "Rooms"].split(",")
    }


def find_header_row(xls, sheet_name):
    """
    Scan the sheet row-by-row for the row containing 'Category'.
    Returns the integer row index to pass as header= to xls.parse().
    Returns None if not found.
    """
    raw_df = xls.parse(sheet_name, header=None)
    for i, row in raw_df.iterrows():
        row_values = [str(v).strip() for v in row.values]
        if "Category" in row_values:
            return i
    return None


def count_unique_lab_days(xls):
    """
    Count unique entries in the 'Week' column of ExperimentIndex.
    Each unique Week value represents a distinct lab day (or date block).
    This is used for glove cost estimation — we want the number of days
    students are actually in the lab, NOT the number of experiments.
    """
    try:
        index_df = xls.parse("ExperimentIndex")
        index_df.columns = index_df.columns.str.strip()
        unique_weeks = index_df["Week"].dropna().astype(str).str.strip()
        unique_weeks = unique_weeks[unique_weeks.str.lower() != "nan"]
        return unique_weeks.nunique()
    except Exception as e:
        print(f"Warning: Could not count lab days from ExperimentIndex: {e}")
        return 0


def gather_all_items_for_file(file_path):
    """
    Load all experiments from a single *Experiments.xlsx file.
    Returns (course_name, course_info, experiments_dict, num_lab_days).
    """
    course_name = os.path.basename(file_path).split("Experiments.xlsx")[0].strip("_").strip()
    xls = pd.ExcelFile(file_path)

    course_df   = xls.parse("CourseInfo")
    course_info = load_course_info(course_df)

    num_lab_days = count_unique_lab_days(xls)

    experiment_list_df = xls.parse("ExperimentIndex")
    experiment_list_df.columns = experiment_list_df.columns.str.strip()

    experiments = {}
    for _, row in experiment_list_df.iterrows():
        exp_title  = str(row["Experiment Title"])
        sheet_name = str(row["SheetName"])
        if sheet_name.endswith('.0'):
            sheet_name = sheet_name[:-2]
        sheet_name = sheet_name.strip()

        xls_sheet_names = [s.strip() for s in xls.sheet_names]
        if sheet_name not in xls_sheet_names:
            print(f"  WARNING: Sheet '{sheet_name}' missing in {course_name} — skipping.")
            continue

        header_row = find_header_row(xls, sheet_name)
        if header_row is None:
            print(f"  WARNING: No 'Category' header found in sheet '{sheet_name}' "
                  f"of {course_name} — skipping.")
            continue

        exp_df = xls.parse(sheet_name, header=header_row)
        exp_df.columns = exp_df.columns.str.strip()
        exp_df.sheet_name = sheet_name
        experiments[exp_title] = exp_df

    return course_name, course_info, experiments, num_lab_days


def gather_all_courses():
    """
    Find every *Experiments.xlsx file in ExpFiles and load each one.
    Returns a list of (course_name, course_info, experiments_dict, num_lab_days).
    """
    folder_path = r"C:\Users\Kandriad\Desktop\ExpFiles"
    pattern     = os.path.join(folder_path, "*Experiments.xlsx")
    files       = glob.glob(pattern)

    if not files:
        raise FileNotFoundError(f"No *Experiments.xlsx files found in: {folder_path}")

    print(f"Found {len(files)} course file(s):")
    for f in files:
        print(f"  {os.path.basename(f)}")
    print()

    all_courses = []
    for file_path in files:
        try:
            all_courses.append(gather_all_items_for_file(file_path))
        except Exception as e:
            print(f"ERROR loading {os.path.basename(file_path)}: {e}")

    return all_courses


# ----------------------------
# LIBRARY LOOKUP
# ----------------------------
def lookup_by_name_or_key(name, library_dict, lib_label="item",
                          sheet_name=None, exp_title=None):
    if not name or str(name).lower() == "nan":
        return None
    name_lower = str(name).strip().lower()

    for key, info in library_dict.items():
        if key.strip().lower() == name_lower:
            return info
        if str(info.get("name", "")).strip().lower() == name_lower:
            return info
        synonyms = info.get("synonyms") or info.get("synonym")
        if synonyms:
            if isinstance(synonyms, str):
                synonyms = [synonyms]
            if any(str(s).strip().lower() == name_lower for s in synonyms):
                return info

    context = ""
    if sheet_name:
        context += f" in sheet {sheet_name}"
    if exp_title:
        context += f" (experiment: '{exp_title}')"
    print(f"  Warning: '{name}' not found in {lib_label} library{context}")
    return None


def validate_item(name, category, sheet_name=None, exp_title=None):
    if category == "Biological":
        return lookup_by_name_or_key(name, bacteria.bacteria_list,    "bacteria",   sheet_name, exp_title)
    elif category == "Uninoculated Media":
        return lookup_by_name_or_key(name, media.media_list,          "media",      sheet_name, exp_title)
    elif category == "Chemical":
        return lookup_by_name_or_key(name, chemicals.chemical_list,   "chemical",   sheet_name, exp_title)
    elif category == "Supply":
        return lookup_by_name_or_key(name, supplies.supplies,         "supply",     sheet_name, exp_title)
    elif category == "Antibiotics":
        return lookup_by_name_or_key(name, antibiotics.antibiotics,   "antibiotic", sheet_name, exp_title)
    return None


# ----------------------------
# QUANTITY VALIDATION
# ----------------------------
def parse_quantity(quantity_raw, sheet_name=None, exp_title=None, item_name=None):
    try:
        return float(quantity_raw)
    except (ValueError, TypeError):
        raise ValueError(
            f"Invalid quantity '{quantity_raw}' in sheet '{sheet_name}', "
            f"experiment '{exp_title}', item '{item_name}'. Must be a number."
        )


# ----------------------------
# COST + QUANTITY CALCULATIONS
# ----------------------------
def calculate_total_qty(quantity, dist_type, course_info, form=None):
    multiplier = {
        "Per Student": course_info["students"],
        "Per Pair":    course_info["students"] // 2,
        "Per Group":   course_info["groups"],
        "Per Section": course_info["sections"],
        "Per Table":   sum(5 if room.strip() == "113" else 6 for room in course_info["rooms"]),
        "Per Room":    len(course_info["rooms"]),
        "Per Course":  1
    }.get(dist_type, 1)
    return quantity * multiplier


def get_cost_per_use(info_dict):
    if info_dict is None:
        return 0
    cost = info_dict.get("cost_per_unit") or info_dict.get("cost_per_ml")
    qty  = info_dict.get("quantity", 1)
    if cost is None or qty in [0, None]:
        return 0
    return float(cost) / float(qty)


def calculate_item_cost(row, course_info, exp_title=None, sheet_name=None):
    """
    Calculate the total cost for a single item row, including both the base
    material cost AND any container/vessel cost determined by the item's form.

    Container cost confirmation:
      form == plate
          → base cost (media volume × cost_per_ml)
          + petri dish cost (slippable for NA/TSA/MA/R2A; standard otherwise)  ✅

      form == microcentrifuge_tube
          → base cost (material cost)
          + Microcentrifuge Tube, 1.5 mL cost from supply library              ✅

      form == durham_tube
          → base cost (broth/media volume × cost_per_ml)
          + Durham Tube cost from supply library                                ✅
    """
    category   = str(row.get("Category", "")).strip()
    name       = str(row.get("Item/Organism", "")).strip()
    dist_type  = str(row.get("DistributionType", "")).title()
    quantity   = parse_quantity(row.get("Quantity"), sheet_name, exp_title, name)
    form       = row.get("Form", None)
    form_str   = str(form).strip() if form else ""
    form_lower = form_str.lower()

    total_samples = calculate_total_qty(quantity, dist_type, course_info, form_str)

    base_cost  = 0
    media_name = ""

    if category == "Biological":
        media_name = str(row.get("Media Used", "")).strip()
        if not media_name:
            print(f"  Missing media for biological '{name}' in {sheet_name}")
            return 0
        media_info = validate_item(media_name, "Uninoculated Media", sheet_name, exp_title)
        if not media_info:
            return 0
        volume_ml = media.standard_volumes_ml.get(form_str, 1)
        base_cost = total_samples * volume_ml * media_info.get("cost_per_ml", 0)

    elif category == "Uninoculated Media":
        media_name = str(row.get("Media Used", "")).strip()
        if not media_name:
            print(f"  Missing media name in sheet {sheet_name}, experiment {exp_title}")
            return 0
        item_info = validate_item(media_name, "Uninoculated Media", sheet_name, exp_title)
        if not item_info:
            return 0
        volume_ml = media.standard_volumes_ml.get(form_str, 1)
        base_cost = total_samples * volume_ml * item_info.get("cost_per_ml", 0)

    elif category == "Chemical":
            item_info = validate_item(name, "Chemical", sheet_name, exp_title)
            if not item_info:
                return 0
            if form_lower == "1_ul":
                # Library cost_per_unit is priced over `quantity` which is in mL.
                # 1 µL = 0.001 mL, so scale the cost-per-mL down accordingly.
                cost_per_ml = get_cost_per_use(item_info)   # cost per 1 mL
                cost_per_ul = cost_per_ml * 0.001            # cost per 1 µL
                base_cost   = total_samples * cost_per_ul
            else:
                volume_ml = media.standard_volumes_ml.get(form_str, 1)
                base_cost = total_samples * volume_ml * get_cost_per_use(item_info)

    elif category in ["Supply", "Antibiotics"]:
        item_info = validate_item(name, category, sheet_name, exp_title)
        if not item_info:
            return 0
        base_cost = total_samples * get_cost_per_use(item_info)

    # ------------------------------------------------------------------
    # Container cost — added on top of base_cost for all categories.
    # This ensures e.g. a biological item in a microcentrifuge tube still
    # picks up the tube cost, regardless of the base cost category branch.
    # ------------------------------------------------------------------
    container_cost = 0

    if form_lower == "plate":
        media_upper = media_name.upper() if media_name else ""
        if media_upper in ["NA", "TSA", "MA", "R2A"]:
            petri_info = validate_item(
                "Empty Petri Dish, 100mm, Slippable", "Supply", sheet_name, exp_title)
        else:
            petri_info = validate_item(
                "Empty Petri Dish, 100mm", "Supply", sheet_name, exp_title)
        if petri_info:
            container_cost += total_samples * get_cost_per_use(petri_info)

    elif form_lower == "microcentrifuge_tube":
        tube_info = validate_item(
            "Microcentrifuge Tube, 1.5 mL", "Supply", sheet_name, exp_title)
        if tube_info:
            container_cost += total_samples * get_cost_per_use(tube_info)

    elif form_lower == "durham_tube":
        durham_info = validate_item(
            "Durham Tube", "Supply", sheet_name, exp_title)
        if durham_info:
            container_cost += total_samples * get_cost_per_use(durham_info)

    return base_cost + container_cost


def calculate_experiment_cost(experiment_df, course_info, exp_title, sheet_name):
    total_cost     = 0
    itemized_costs = []
    zero_cost_items = []

    for _, row in experiment_df.iterrows():
        category = str(row.get("Category", "")).strip()
        if not category or category.lower() == "nan":
            continue

        try:
            cost     = calculate_item_cost(row, course_info, exp_title, sheet_name)
            quantity = parse_quantity(
                row.get("Quantity"), sheet_name, exp_title, row.get("Item/Organism"))

            if category == "Uninoculated Media":
                item_name  = str(row.get("Media Used", "")).strip()
                media_used = item_name
            else:
                item_name  = str(row.get("Item/Organism", "")).strip()
                media_used = (str(row.get("Media Used", "")).strip()
                              if category == "Biological" else "")

            form      = row.get("Form", None)
            dist_type = str(row.get("DistributionType", "")).title()
            total_units = calculate_total_qty(quantity, dist_type, course_info, form)

            itemized_costs.append((item_name, media_used, form, total_units, cost, category))
            total_cost += cost

            if cost == 0 and item_name:
                zero_cost_items.append((item_name, category))

        except Exception as e:
            print(f"  Error calculating cost for "
                  f"'{row.get('Item/Organism', '')}' in {sheet_name}: {e}")

    return total_cost, itemized_costs, zero_cost_items


def calculate_course_cost(experiments_dict, course_info):
    breakdowns  = {}
    grand_total = 0.0

    for exp_title, exp_df in experiments_dict.items():
        sheet_name = getattr(exp_df, 'sheet_name', exp_title)
        try:
            total, itemized, zero_cost = calculate_experiment_cost(
                exp_df, course_info, exp_title, sheet_name)
        except Exception as e:
            print(f"  Error in experiment '{exp_title}': {e}")
            total, itemized, zero_cost = 0.0, [], []

        if total is None or total != total:   # NaN guard
            total = 0.0

        breakdowns[exp_title] = {
            "items":           itemized,
            "experiment_total": total,
            "zero_cost_items": zero_cost
        }
        grand_total += total

    return grand_total, breakdowns


# ----------------------------
# GLOVE COST ESTIMATE
# ----------------------------
# Shifted bell curve: majority Medium, then Small, L and XS roughly equal, XL rare.
GLOVE_PROPORTIONS = {
    "XS": 0.07,
    "S":  0.28,
    "M":  0.45,
    "L":  0.15,
    "XL": 0.05,
}

# Supply library keys for each glove size.
GLOVE_SUPPLY_KEYS = {
    "XS": "gloves_xs",
    "S":  "gloves_s",
    "M":  "gloves_m",
    "L":  "gloves_l",
    "XL": "gloves_xl",
}

# Each box contains 100 gloves = 50 pairs.
GLOVES_PER_BOX  = 100
PAIRS_PER_BOX   = GLOVES_PER_BOX // 2   # 50

# Usage rate: every person uses 1 guaranteed pair per lab day, and on average
# half of all students grab a second pair — so the expected usage is 1.5 pairs
# per person per lab day.
PAIRS_PER_PERSON_PER_DAY = 1.5


def get_glove_cost_per_pair(size_key):
    """
    Look up a glove size in the supply library and return the cost per pair.

    Supply library structure:
      cost_per_unit  = price per case
      quantity       = boxes per case  (each box = 100 gloves = 50 pairs)

    cost per box  = cost_per_unit / quantity
    cost per pair = cost per box  / PAIRS_PER_BOX
    """
    info = supplies.supplies.get(size_key)
    if not info:
        print(f"  Warning: Glove size key '{size_key}' not found in supply library.")
        return 0.0
    cost_per_case = float(info.get("cost_per_unit", 0))
    boxes_per_case = float(info.get("quantity", 1))
    if boxes_per_case == 0:
        return 0.0
    cost_per_box  = cost_per_case / boxes_per_case
    cost_per_pair = cost_per_box  / PAIRS_PER_BOX
    return cost_per_pair


def estimate_glove_cost(num_students, num_lab_days):
    """
    Estimate total semester glove cost, broken down by size.

      People counted  = num_students + 1 TA
      Pairs used      = people × PAIRS_PER_PERSON_PER_DAY × num_lab_days
                        (1 guaranteed pair + ~0.5 extra for the ~half who take a second)
      Cost per pair   = looked up from the supply library per size
      Size split      = shifted bell curve (peak M, skewed toward S)

    Returns (total_cost, size_breakdown_dict, total_effective_pairs).
    """
    total_people         = num_students + 1
    total_effective_pairs = total_people * PAIRS_PER_PERSON_PER_DAY * num_lab_days

    size_breakdown = {}
    total_cost     = 0.0

    for size, proportion in GLOVE_PROPORTIONS.items():
        supply_key       = GLOVE_SUPPLY_KEYS[size]
        cost_per_pair    = get_glove_cost_per_pair(supply_key)
        people_this_size = round(total_people * proportion)
        pairs_this_size  = people_this_size * PAIRS_PER_PERSON_PER_DAY * num_lab_days
        cost_this_size   = pairs_this_size * cost_per_pair

        size_breakdown[size] = {
            "people":      people_this_size,
            "total_pairs": pairs_this_size,
            "cost_per_pair": cost_per_pair,
            "cost":        cost_this_size
        }
        total_cost += cost_this_size

    return total_cost, size_breakdown, total_effective_pairs


# ----------------------------
# WORD DOCUMENT EXPORT
# ----------------------------
def build_title(course_name):
    return f"{course_name} Cost Analysis — {datetime.today().strftime('%B %Y')}"


def add_run(para, text, bold=False, italic=False, font_size=10,
            font_name="Consolas", color=None, underline=False):
    run           = para.add_run(text)
    run.bold      = bold
    run.italic    = italic
    run.underline = underline
    run.font.name = font_name
    run.font.size = Pt(font_size)
    if color:
        run.font.color.rgb = RGBColor(*color)
    return run


ORANGE = (0xC0, 0x50, 0x00)
GRAY   = (0x70, 0x70, 0x70)


def export_cost_assessment(course_name, course_info, experiments_dict,
                           grand_total, breakdowns, num_lab_days):
    doc   = Document()
    style = doc.styles['Normal']
    style.font.name = 'Consolas'
    style.font.size = Pt(11)

    num_students = course_info["students"]

    # ── Title ──────────────────────────────────────────────────────────
    title_para = doc.add_heading(level=1)
    t_run = title_para.add_run(build_title(course_name))
    t_run.bold           = True
    t_run.font.name      = 'Consolas'
    t_run.font.size      = Pt(16)
    title_para.alignment = 1

    # ── Course Information ─────────────────────────────────────────────
    doc.add_heading("Course Information", level=2)
    doc.add_paragraph(
        f"Students: {course_info['students']} | "
        f"Sections: {course_info['sections']} | "
        f"Groups: {course_info['groups']} | "
        f"Rooms: {', '.join(course_info['rooms'])} | "
        f"Lab Days: {num_lab_days}"
    )

    # ── Total Course Cost ──────────────────────────────────────────────
    doc.add_heading("Total Course Cost", level=2)

    cost_para = doc.add_paragraph()
    add_run(cost_para, f"${grand_total:.2f}  ", bold=True, font_size=12)
    if num_students > 0:
        add_run(cost_para,
                f"(${grand_total / num_students:.2f} per student)",
                font_size=11)

    # ── Disclaimer ─────────────────────────────────────────────────────
    disc = doc.add_paragraph()
    disc.paragraph_format.space_before = Pt(6)
    disc.paragraph_format.space_after  = Pt(6)
    add_run(
        disc,
        "Note: This analysis does not include facility costs or glove usage costs.",
        italic=True, font_size=10, color=GRAY
    )

    # ── Glove Cost Estimate ────────────────────────────────────────────
    doc.add_heading("Estimated Glove Cost (Semester)", level=2)

    glove_total, size_breakdown, total_pairs = estimate_glove_cost(
        num_students, num_lab_days)
    total_people = num_students + 1

    intro = doc.add_paragraph()
    add_run(
        intro,
        f"{num_students} students + 1 TA = {total_people} people × "
        f"{PAIRS_PER_PERSON_PER_DAY} pairs/person/day × {num_lab_days} lab day(s). "
        f"(1 guaranteed pair + ~0.5 extra for the ~half of students who take a second pair.) "
        f"Size distribution: shifted bell curve (peak at M, skewed toward S; "
        f"L \u2248 XS; XL \u2248 1 person). Glove costs sourced from supply library.",
        italic=True, font_size=10, color=GRAY
    )

    total_line = doc.add_paragraph()
    add_run(total_line, "Estimated total:  ", font_size=10)
    add_run(total_line, f"${glove_total:.2f}", bold=True, font_size=11)
    add_run(total_line, f"  ({total_pairs:.0f} effective pairs)", font_size=10, color=GRAY)

    for size, d in size_breakdown.items():
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Pt(18)
        p.paragraph_format.space_after = Pt(0)
        add_run(
            p,
            f"{size:<4}  ~{d['people']:>3} people  ×  {PAIRS_PER_PERSON_PER_DAY} pairs/day"
            f"  ×  {num_lab_days} days  =  {d['total_pairs']:>5.1f} pairs"
            f"  @  ${d['cost_per_pair']:.4f}/pair   =  ${d['cost']:>7.2f}",
            font_size=10
        )

    # ── Combined Total (supplies + gloves) ────────────────────────────
    combined_total = grand_total + glove_total
    combined_para  = doc.add_paragraph()
    combined_para.paragraph_format.space_before = Pt(8)
    add_run(combined_para, "Estimated Total (supplies + gloves):  ", font_size=11)
    add_run(combined_para, f"${combined_total:.2f}", bold=True, font_size=12)
    if num_students > 0:
        add_run(combined_para,
                f"  (${combined_total / num_students:.2f} per student)",
                font_size=11)

    # ── Experiment Costs ───────────────────────────────────────────────
    doc.add_heading("Experiment Costs", level=2)

    for exp_title, data in breakdowns.items():
        items           = data["items"]
        exp_total       = data["experiment_total"]
        zero_cost_items = data["zero_cost_items"]
        sheet_name      = getattr(experiments_dict[exp_title], 'sheet_name', exp_title)

        exp_hdr = doc.add_heading(level=3)
        exp_per_student = (exp_total / num_students) if num_students > 0 else 0
        hdr_run = exp_hdr.add_run(
            f"{sheet_name} — {exp_title}  "
            f"(Total: ${exp_total:.2f} | ${exp_per_student:.2f}/student)"
        )
        hdr_run.bold      = True
        hdr_run.font.name = 'Consolas'
        hdr_run.font.size = Pt(11)

        items_by_category = {}
        for row_tuple in items:
            item_name, media_used, form, total_units, item_cost, category = row_tuple
            items_by_category.setdefault(category, []).append(
                (item_name, media_used, form, total_units, item_cost))

        for category, cat_items in items_by_category.items():
            cat_p = doc.add_paragraph()
            cat_p.paragraph_format.left_indent = Pt(12)
            cat_p.paragraph_format.space_after = Pt(0)
            cr = cat_p.add_run(category)
            cr.font.name  = 'Consolas'
            cr.font.size  = Pt(10)
            cr.underline  = True

            for item_name, media_used, form, total_units, item_cost in cat_items:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Pt(24)
                p.paragraph_format.space_after = Pt(0)

                r1 = p.add_run(f"{item_name}")
                r1.font.name = 'Consolas'
                r1.font.size = Pt(10)
                if category == "Biological":
                    r1.italic = True

                media_text = (
                    f" — Media: {media_used}"
                    if category in ["Biological", "Uninoculated Media"] and media_used
                    else ""
                )
                form_text = (
                    f", Form: {form}"
                    if category in ["Biological", "Uninoculated Media", "Chemical"]
                    else ""
                )

                r2 = p.add_run(f"{media_text}{form_text}, Qty: {total_units}, ")
                r2.font.name = 'Consolas'
                r2.font.size = Pt(10)

                r3 = p.add_run(f"Cost: ${item_cost:.2f}")
                r3.font.name = 'Consolas'
                r3.font.size = Pt(10)
                r3.bold      = True
                if item_cost == 0:
                    r3.font.color.rgb = RGBColor(*ORANGE)

        if zero_cost_items:
            notice = doc.add_paragraph()
            notice.paragraph_format.left_indent  = Pt(12)
            notice.paragraph_format.space_before = Pt(4)
            wr = notice.add_run("⚠ No cost data found for: ")
            wr.font.name       = 'Consolas'
            wr.font.size       = Pt(9)
            wr.bold            = True
            wr.font.color.rgb  = RGBColor(*ORANGE)
            dr = notice.add_run(
                "; ".join(f"{n} ({c})" for n, c in zero_cost_items))
            dr.font.name       = 'Consolas'
            dr.font.size       = Pt(9)
            dr.font.color.rgb  = RGBColor(*ORANGE)

    filename = f"{build_title(course_name)}.docx"
    doc.save(filename)
    print(f"  Saved: {filename}")
    return filename


# ----------------------------
# MAIN EXECUTION
# ----------------------------
if __name__ == "__main__":
    all_courses = gather_all_courses()

    if not all_courses:
        print("No courses loaded — exiting.")
        sys.exit(1)

    print(f"Generating Word documents for {len(all_courses)} course(s)...\n")

    for course_name, course_info, experiments, num_lab_days in all_courses:
        print(f"Processing: {course_name}  "
              f"({course_info['students']} students, {num_lab_days} lab days)")
        grand_total, breakdowns = calculate_course_cost(experiments, course_info)
        export_cost_assessment(
            course_name, course_info, experiments,
            grand_total, breakdowns, num_lab_days
        )

    print("\nAll done!")