import sys
import pandas as pd
import glob
import os
from docx import Document
from docx.shared import Pt
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
        "groups": int(course_df.loc[0, "Groups"]),
        "rooms": course_df.loc[0, "Rooms"].split(",")
    }

def gather_all_items():
    folder_path = r"C:\Users\Kandriad\Desktop\ExpFiles"
    pattern = os.path.join(folder_path, "*Experiments.xlsx")
    experiment_files = glob.glob(pattern)

    if not experiment_files:
        raise FileNotFoundError("No *Experiments.xlsx files found.")

    file = experiment_files[0]
    course_name = os.path.basename(file).split("Experiments.xlsx")[0].strip("_")
    xls = pd.ExcelFile(file)

    course_df = xls.parse("CourseInfo")
    course_info = load_course_info(course_df)

    experiment_list_df = xls.parse("ExperimentIndex")
    experiment_list_df.columns = experiment_list_df.columns.str.strip()

    experiments = {}
    for _, row in experiment_list_df.iterrows():
        exp_title = str(row["Experiment Title"])
        sheet_name = str(row["SheetName"])
        if sheet_name.endswith('.0'):
            sheet_name = sheet_name[:-2]

        if sheet_name not in xls.sheet_names:
            print(f"WARNING: Sheet '{sheet_name}' missing — skipping.")
            continue

        exp_df = xls.parse(sheet_name)
        exp_df.columns = exp_df.columns.str.strip()
        exp_df.sheet_name = sheet_name  # attach sheet_name to df
        experiments[exp_title] = exp_df

    return course_name, course_info, experiments

# ----------------------------
# LIBRARY LOOKUP
# ----------------------------
def lookup_by_name_or_key(name, library_dict, lib_label="item", sheet_name=None, exp_title=None):
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
        context += f" Experiment: '{exp_title}'"
    print(f"Warning: '{name}' not found in {lib_label} library{context}")
    return None

def validate_item(name, category, sheet_name=None, exp_title=None):
    if category == "Biological":
        return lookup_by_name_or_key(name, bacteria.bacteria_list, "bacteria", sheet_name, exp_title)
    elif category == "Uninoculated Media":
        return lookup_by_name_or_key(name, media.media_list, "media", sheet_name, exp_title)
    elif category == "Chemical":
        return lookup_by_name_or_key(name, chemicals.chemical_list, "chemical", sheet_name, exp_title)
    elif category == "Supply":
        return lookup_by_name_or_key(name, supplies.supplies, "supply", sheet_name, exp_title)
    elif category == "Antibiotics":
        return lookup_by_name_or_key(name, antibiotics.antibiotics, "antibiotic", sheet_name, exp_title)
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
            f"experiment '{exp_title}', item '{item_name}'. Quantity must be a number."
        )

# ----------------------------
# COST + QUANTITY CALCULATIONS
# ----------------------------
def calculate_total_qty(quantity, dist_type, course_info, form=None):
    multiplier = {
        "Per Student": course_info["students"],
        "Per Pair": course_info["students"] // 2,
        "Per Group": course_info["groups"],
        "Per Section": course_info["sections"],
        "Per Table": sum(5 if room.strip() == "113" else 6 for room in course_info['rooms']),
        "Per Room": len(course_info["rooms"]),
        "Per Course": 1
    }.get(dist_type, 1)
    return quantity * multiplier

def get_cost_per_use(info_dict):
    if info_dict is None:
        return 0
    cost = info_dict.get("cost_per_unit") or info_dict.get("cost_per_ml")
    qty = info_dict.get("quantity", 1)
    if cost is None or qty in [0, None]:
        return 0
    return float(cost) / float(qty)

def calculate_item_cost(row, course_info, exp_title=None, sheet_name=None):
    category = str(row.get("Category", "")).strip()
    name = str(row.get("Item/Organism", "")).strip()
    dist_type = str(row.get("DistributionType", "")).title()
    quantity = parse_quantity(row.get("Quantity"), sheet_name, exp_title, name)
    form = row.get("Form", None)
    total_samples = calculate_total_qty(quantity, dist_type, course_info, form)

    base_cost = 0
    media_name = ""

    if category == "Biological":
        media_name = str(row.get("Media Used", "")).strip()
        if not media_name:
            print(f"Missing media for biological '{name}' in {sheet_name}")
            return 0
        media_info = validate_item(media_name, "Uninoculated Media", sheet_name, exp_title)
        if not media_info:
            return 0
        volume_ml = media.standard_volumes_ml.get(form, 1)
        base_cost = total_samples * volume_ml * media_info.get("cost_per_ml", 0)

    elif category == "Uninoculated Media":
        media_name = str(row.get("Media Used", "")).strip()
        if not media_name:
            print(f"Missing media name in sheet {sheet_name}, experiment {exp_title}")
            return 0
        item_info = validate_item(media_name, "Uninoculated Media", sheet_name, exp_title)
        if not item_info:
            return 0
        volume_ml = media.standard_volumes_ml.get(form, 1)
        base_cost = total_samples * volume_ml * item_info.get("cost_per_ml", 0)

    elif category == "Chemical":
        item_info = validate_item(name, "Chemical", sheet_name, exp_title)
        if not item_info:
            return 0
        volume_ml = media.standard_volumes_ml.get(form, 1)
        base_cost = total_samples * volume_ml * get_cost_per_use(item_info)

    elif category in ["Supply", "Antibiotics"]:
        item_info = validate_item(name, category, sheet_name, exp_title)
        if not item_info:
            return 0
        base_cost = total_samples * get_cost_per_use(item_info)

    # Container cost
    container_cost = 0
    form_lower = str(form).lower()
    if form_lower == "plate":
        media_upper = media_name.upper() if media_name else ""
        if media_upper not in ["NA", "TSA", "MA", "R2A"]:
            petri_info = validate_item("Empty Petri Dish, 100mm", "Supply", sheet_name, exp_title)
        else:
            petri_info = validate_item("Empty Petri Dish, 100mm, Slippable", "Supply", sheet_name, exp_title)
        if petri_info:
            container_cost += total_samples * get_cost_per_use(petri_info)
    elif form_lower == "microcentrifuge_tube":
        tube_info = validate_item("Microcentrifuge Tube, 1.5 mL", "Supply", sheet_name, exp_title)
        if tube_info:
            container_cost += total_samples * get_cost_per_use(tube_info)
    elif form_lower == "durham_tube":
        durham_info = validate_item("Durham Tube", "Supply", sheet_name, exp_title)
        if durham_info:
            container_cost += total_samples * get_cost_per_use(durham_info)

    return base_cost + container_cost

def calculate_experiment_cost(experiment_df, course_info, exp_title, sheet_name):
    total_cost = 0
    itemized_costs = []
    for _, row in experiment_df.iterrows():
        try:
            cost = calculate_item_cost(row, course_info, exp_title, sheet_name)
            quantity = parse_quantity(row.get("Quantity"), sheet_name, exp_title, row.get("Item/Organism"))
            category = str(row.get("Category", "")).strip()
            if category == "Uninoculated Media":
                item_name = str(row.get("Media Used", "")).strip()
                media_used = item_name
            else:
                item_name = str(row.get("Item/Organism", "")).strip()
                media_used = str(row.get("Media Used", "")).strip() if category == "Biological" else ""
            form = row.get("Form", None)
            dist_type = str(row.get("DistributionType", "")).title()
            total_units = calculate_total_qty(quantity, dist_type, course_info, form)
            itemized_costs.append((item_name, media_used, form, total_units, cost, category))
            total_cost += cost
        except Exception as e:
            print(f"Error calculating cost for '{row.get('Item/Organism', '')}' in {sheet_name}: {e}")
    return total_cost, itemized_costs

def calculate_course_cost(experiments_dict, course_info):
    breakdowns = {}
    grand_total = 0.0  # make sure it starts as float
    for exp_title, exp_df in experiments_dict.items():
        sheet_name = getattr(exp_df, 'sheet_name', exp_title)
        try:
            total, itemized = calculate_experiment_cost(exp_df, course_info, exp_title, sheet_name)
        except Exception as e:
            print(f"Error calculating cost for experiment '{exp_title}': {e}")
            total, itemized = 0.0, []

        # Ensure total is numeric
        if total is None or total != total:  # check for NaN
            total = 0.0

        breakdowns[exp_title] = {
            "items": itemized,
            "experiment_total": total
        }
        grand_total += total

    return grand_total, breakdowns

# ----------------------------
# WORD DOCUMENT EXPORT
# ----------------------------
def build_title(course_name):
    date_str = datetime.today().strftime("%B %Y")
    return f"{course_name} Cost Analysis — {date_str}"

def export_cost_assessment(course_name, course_info, experiments_dict, grand_total, breakdowns):
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Consolas'
    style.font.size = Pt(11)

    # Title
    title = doc.add_heading(level=1)
    run = title.add_run(build_title(course_name))
    run.bold = True
    run.font.name = 'Consolas'
    run.font.size = Pt(16)
    title.alignment = 1  # 0=left, 1=center, 2=right, 3=justify

    # Course Information
    doc.add_heading("Course Information", level=2)
    course_info_text = (
        f"Students: {course_info['students']} | "
        f"Sections: {course_info['sections']} | "
        f"Groups: {course_info['groups']} | "
        f"Rooms: {', '.join(course_info['rooms'])}"
    )
    doc.add_paragraph(course_info_text)

    # Total Course Cost
    doc.add_heading("Total Course Cost", level=2)
    para = doc.add_paragraph()
    run = para.add_run(f"${grand_total:.2f}")
    run.bold = True
    run.font.name = 'Consolas'
    run.font.size = Pt(12)

    # Experiment Costs
    doc.add_heading("Experiment Costs", level=2)
    for exp_title, data in breakdowns.items():
        items = data["items"]
        exp_total = data["experiment_total"]
        sheet_name = getattr(experiments_dict[exp_title], 'sheet_name', exp_title)
        
        header = doc.add_heading(level=3)
        run = header.add_run(f"{sheet_name} — {exp_title} (Total: ${exp_total:.2f})")
        run.bold = True
        run.font.name = 'Consolas'
        run.font.size = Pt(11)

        # Items by category
        items_by_category = {}
        for item_name, media_used, form, total_units, item_cost, category in items:
            items_by_category.setdefault(category, []).append((item_name, media_used, form, total_units, item_cost))

        for category, items in items_by_category.items():
            # Category header, indented once
            cat_para = doc.add_paragraph()
            cat_para.paragraph_format.left_indent = Pt(12)
            cat_run = cat_para.add_run(category)
            cat_run.font.name = 'Consolas'
            cat_run.font.size = Pt(10)
            cat_run.underline = True
            cat_para.paragraph_format.space_after = Pt(0)

            for item_name, media_used, form, total_units, item_cost in items:
                para = doc.add_paragraph()
                para.paragraph_format.left_indent = Pt(24)
                run1 = para.add_run(f"{item_name}")
                run1.font.name = 'Consolas'
                run1.font.size = Pt(10)
                if category == "Biological":
                    run1.italic = True

                media_text = f" — Media: {media_used}" if category in ["Biological", "Uninoculated Media"] and media_used else ""
                form_text = f", Form: {form}" if category in ["Biological", "Uninoculated Media", "Chemical"] else ""

                run2 = para.add_run(f"{media_text}{form_text}, Qty: {total_units}, ")
                run2.font.name = 'Consolas'
                run2.font.size = Pt(10)

                run3 = para.add_run(f"Cost: ${item_cost:.2f}")
                run3.font.name = 'Consolas'
                run3.font.size = Pt(10)
                run3.bold = True

                para.paragraph_format.space_after = Pt(0)

    doc.save(f"{build_title(course_name)}.docx")

# ----------------------------
# MAIN EXECUTION
# ----------------------------
if __name__ == "__main__":
    course_name, course_info, experiments = gather_all_items()
    grand_total, breakdowns = calculate_course_cost(experiments, course_info)
    export_cost_assessment(course_name, course_info, experiments, grand_total, breakdowns)
    print("Word document created with detailed breakdown!")
