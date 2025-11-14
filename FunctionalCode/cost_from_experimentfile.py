import os
import sys
import glob
import pandas as pd

# Add libraries path
script_dir = os.path.dirname(os.path.abspath(__file__))
libraries_path = os.path.join(script_dir, "..", "Libraries")
if libraries_path not in sys.path:
    sys.path.append(libraries_path)

import bacteria
import media
import supplies
import antibiotics
import chemicals

special_forms = ["1_ml", "0.5_ml", "1_ul"]

# === Helper: course info ===
def load_course_info(course_df):
    return {
        "students": int(course_df.loc[0, "Students"]),
        "sections": int(course_df.loc[0, "Sections"]),
        "groups": int(course_df.loc[0, "Groups"]),
        "rooms": course_df.loc[0, "Rooms"].split(", ")
    }

# === Helper: total quantity calculation ===
def calculate_total_qty(quantity, dist_type, course_info, form=None):
    multiplier = {
        "Per Student": course_info["students"],
        "Per Pair": course_info["students"] // 2,
        "Per Group": course_info["groups"],
        "Per Table": sum(5 if room.strip() == "113" else 6 for room in course_info['rooms']),
        "Per Section": course_info["sections"],
        "Per Room": len(course_info["rooms"]),
        "Per Course": 1
    }.get(dist_type, 1)
    
    if form in special_forms:
        return multiplier
    return quantity * multiplier

# === Lookup with synonyms ===
def lookup_by_name_or_key(name, library_dict):
    if not name or str(name).lower() == "nan":
        return None
    name_lower = str(name).strip().lower()
    for key, info in library_dict.items():
        # match key
        if key.strip().lower() == name_lower:
            return info
        # match name field
        if str(info.get("name", "")).strip().lower() == name_lower:
            return info
        # match synonyms
        synonyms = info.get("synonyms", [])
        if any(str(s).strip().lower() == name_lower for s in synonyms):
            return info
    return None

# === Unit cost lookup using library ===
def get_unit_cost(item_name, category, media_used=None):
    if category == "Biological":
        info = lookup_by_name_or_key(item_name, bacteria.bacteria_list)
        cost = info.get("cost", 0) if info else 0
        if media_used:
            media_info = lookup_by_name_or_key(media_used, media.media_list)
            cost += media_info.get("cost_per_ml", 0) if media_info else 0
        return cost

    elif category == "Uninoculated Media":
        info = lookup_by_name_or_key(item_name, media.media_list)
        return info.get("cost_per_ml", 0) if info else 0

    elif category == "Chemical":
        info = lookup_by_name_or_key(item_name, chemicals.chemical_list)
        return info.get("cost_per_unit", 0) if info else 0

    elif category == "Supply":
        info = lookup_by_name_or_key(item_name, supplies.supplies)
        return info.get("cost", 0) if info else 0

    elif category == "Antibiotics":
        info = lookup_by_name_or_key(item_name, antibiotics.antibiotics)
        return info.get("cost", 0) if info else 0

    return 0

# === Cost per row ===
def calculate_item_cost(row, course_info):
    quantity = row.get("Quantity", 0)
    dist_type = str(row.get("DistributionType", "")).title()
    form = row.get("Form", None)
    category = row.get("Category", "")
    media_used = row.get("Media Used", None)

    total_qty = calculate_total_qty(quantity, dist_type, course_info, form)
    unit_cost = get_unit_cost(row.get("Item/Organism"), category, media_used)
    return total_qty * unit_cost

# === Analyze a single course ===
def analyze_course_costs(course_file):
    xls = pd.ExcelFile(course_file)
    course_df = xls.parse("CourseInfo")
    course_info = load_course_info(course_df)

    schedule_df = xls.parse("ExperimentIndex")
    schedule_df.columns = schedule_df.columns.str.strip()

    course_name = os.path.basename(course_file).replace("Experiments.xlsx", "")
    experiment_costs = []

    for _, exp_row in schedule_df.iterrows():
        sheet_name = str(exp_row["SheetName"])
        if sheet_name.endswith('.0'):
            sheet_name = sheet_name[:-2]

        if sheet_name not in xls.sheet_names:
            print(f"Sheet '{sheet_name}' not found in file '{course_file}' — skipping.")
            continue

        exp_df = xls.parse(sheet_name)
        exp_df.columns = exp_df.columns.str.strip()
        exp_title = exp_row["Experiment Title"]

        total_exp_cost = 0
        for _, row in exp_df.iterrows():
            category = str(row.get("Category", "")).strip()
            if not category or str(row.get("Item/Organism", "")).strip() == "":
                continue
            try:
                cost = calculate_item_cost(row, course_info)
                total_exp_cost += cost
            except Exception as e:
                print(f"Error calculating cost for {exp_title} item {row.get('Item/Organism')}: {e}")

        experiment_costs.append({"Experiment": exp_title, "Cost": total_exp_cost})

    total_course_cost = sum(e["Cost"] for e in experiment_costs)
    return course_name, experiment_costs, total_course_cost

# === Analyze all courses in folder ===
def analyze_all_courses(folder_path):
    pattern = os.path.join(folder_path, "*Experiments.xlsx")
    files = glob.glob(pattern)
    all_results = []

    for f in files:
        course_name, exp_costs, course_total = analyze_course_costs(f)
        all_results.append({
            "Course": course_name,
            "Experiments": exp_costs,
            "Total Cost": course_total
        })
    return all_results

# === Run ===
if __name__ == "__main__":
    folder = r"C:\Users\Kandriad\Desktop\ExpFiles"
    results = analyze_all_courses(folder)

    for course in results:
        print(f"\n=== {course['Course']} ===")
        for exp in course['Experiments']:
            print(f"{exp['Experiment']}: ${exp['Cost']:.2f}")
        print(f"Total Course Cost: ${course['Total Cost']:.2f}")
