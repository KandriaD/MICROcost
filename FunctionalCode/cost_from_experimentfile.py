## try to implement cost claculations from gui.py, need it to look up the info like i did there
import sys
import pandas as pd
import glob
import os
from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

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

def load_course_info(course_df):
    return {
        "students": int(course_df.loc[0, "Students"]),
        "sections": int(course_df.loc[0, "Sections"]),
        "groups": int(course_df.loc[0, "Groups"]),
        "rooms": course_df.loc[0, "Rooms"].split(", ")
    }

def caluclate_total_qty(quantity, dist_type, course_info,form=None):
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
    else:
        return quantity * multiplier

def lookup_by_name_or_key(name, library_dict, lib_label="item"):
    name_lower = name.strip().lower()

    for key, info in library_dict.items():
        if key.strip().lower() == name_lower:
            return info
        if info.get("name", "").strip().lower() == name_lower:
            return info
        synonym = info.get("synonyms", [])
        if any(synonyms.strip().lower() == name_lower for synonyms in synonym):
            return info
    print(f"Warning: '{name}' not found in {lib_label} library.")
    return None

def is_valid_bacteria(name):
    return name.strip() in bacteria.bacteria_list  # No change, list of strings

def is_valid_media(name):
    return lookup_by_name_or_key(name.strip(), media.media_list) is not None

def is_valid_supply(name):
    return lookup_by_name_or_key(name.strip(), supplies.supplies) is not None

def is_valid_chemical(name):
    return lookup_by_name_or_key(name.strip(), chemicals.chemical_list) is not None

def is_valid_antibiotic(name):
    return lookup_by_name_or_key(name.strip(), antibiotics.antibiotics) is not None

def validate_item(name, category):
    if category == "Biological":
        return is_valid_bacteria(name)
    elif category == "Uninoculated Media":
        return is_valid_media(name)
    elif category == "Chemical":
        return is_valid_chemical(name)
    elif category == "Supply":
        return is_valid_supply(name)
    elif category == "Antibiotics":
        if not is_valid_antibiotic(name):
            print(f"Warning: Antibiotic '{name}' not found in antibiotics list.")
            return False
        return True
    return False

def gather_all_experiments_for_course(file_path):
    """
    Parses the entire course file: all experiments, all weeks.
    Returns a list of all records (items) from all experiments.
    """
    xls = pd.ExcelFile(file_path)
    course_df = xls.parse("CourseInfo")
    course_info = load_course_info(course_df)
    
    schedule_df = xls.parse("ExperimentIndex")
    schedule_df.columns = schedule_df.columns.str.strip()

    all_records = []
    for _, row in schedule_df.iterrows():
        exp_title = row["Experiment Title"]
        sheet_name = str(row["SheetName"])
        if sheet_name.endswith('.0'):
            sheet_name = sheet_name[:-2]

        if sheet_name not in xls.sheet_names:
            print(f"Sheet '{sheet_name}' not found in file '{file_path}' — skipping.")
            continue

        experiment_df = xls.parse(sheet_name)
        experiment_df.columns = experiment_df.columns.str.strip()

        for _, item in experiment_df.iterrows():
            item_category = str(item.get("Category", "")).strip()
            if not item_category or item_category.lower() == "nan":
                continue

            item_name = item.get("Item/Organism")
            if pd.isna(item_name) and item_category == "Uninoculated Media":
                item_name = item.get("Media Used")
            name = str(item_name).strip() if not pd.isna(item_name) else ""
            media_used = item.get("Media Used", None)
            form = item.get("Form", None)
            quantity = item.get("Quantity", 0)
            dist_type = str(item.get("DistributionType", "")).strip().title()

            try:
                total_qty = caluclate_total_qty(quantity, dist_type, course_info, form)
            except Exception as e:
                print(f"Error calculating quantity for {file_path} {exp_title} - {item_category} {name} {media_used}: {e}")
                continue

            record = {
                "Course": os.path.basename(file_path).replace("Experiments.xlsx", ""),
                "Experiment Title": exp_title,
                "Category": item_category,
                "Item/Organism": name,
                "Media Used": media_used,
                "Form": form,
                "Total Quantity": total_qty,
                "Notes": item.get("Notes", "")
            }
            if form in special_forms:
                record["Volume"] = quantity

            all_records.append(record)
    return all_records

def calculate_cost_from_records(records):
    total_cost = 0
    cost_breakdown = []

    for rec in records:
        category = rec.get("Category", "").strip()
        name = rec.get("Item/Organism", "").strip()
        form = rec.get("Form", "")
        quantity = rec.get("Total Quantity", 0)
        media_used = rec.get("Media Used", "")

        cost = 0
        unit = ""

        if category == "Chemical":
            chem_info = lookup_by_name_or_key(name, chemicals.chemical_list, "chemical")
            if chem_info and "cost_per_ml" in chem_info:
                cost = chem_info["cost_per_ml"] * quantity
                unit = "ml"
        elif category == "Uninoculated Media":
            media_info = lookup_by_name_or_key(name, media.media_list, "media")
            if media_info and "cost_per_ml" in media_info:
                cost = media_info["cost_per_ml"] * quantity
                unit = "ml"
        elif category == "Biological":
            bac_info = lookup_by_name_or_key(name, bacteria.bacteria_list, "bacteria")
            if bac_info and "cost_per_use" in bac_info:
                cost = bac_info["cost_per_use"] * quantity
                unit = "use"
        elif category == "Antibiotics":
            ab_info = lookup_by_name_or_key(name, antibiotics.antibiotics, "antibiotic")
            if ab_info and "cost_per_ml" in ab_info:
                cost = ab_info["cost_per_ml"] * quantity
                unit = "ml"
        elif category == "Supply":
            supp_info = lookup_by_name_or_key(name, supplies.supplies, "supply")
            if supp_info and "cost_each" in supp_info:
                cost = supp_info["cost_each"] * quantity
                unit = "each"

        if cost > 0:
            total_cost += cost
            cost_breakdown.append({
                "Item": name,
                "Category": category,
                "Quantity": quantity,
                "Unit": unit,
                "Cost": round(cost, 2),
                "Form": form,
                "Media Used": media_used
            })
        else:
            print(f"Could not calculate cost for: {name} (category: {category})")

    return total_cost, cost_breakdown

def calculate_cost_for_course(file_path):
    records = gather_all_experiments_for_course(file_path)
    return calculate_cost_from_records(records)

def calculate_cost_for_course_name(course_name):
    folder_path = r"C:\Users\Kandriad\Desktop\ExpFiles"
    pattern = os.path.join(folder_path, f"{course_name}Experiments.xlsx")
    matched_files = glob.glob(pattern)

    if not matched_files:
        print(f"No experiment file found for course '{course_name}'")
        return None, None

    course_file_path = matched_files[0]
    print(f"Calculating costs for course file: {course_file_path}")
    return calculate_cost_for_course(course_file_path)


# Example usage:
if __name__ == "__main__":
    course_name = "461L"  # Change to your course name here
    total, breakdown = calculate_cost_for_course_name(course_name)

    if total is not None:
        print(f"Total cost for course '{course_name}': ${total:.2f}")
        for item in breakdown:
            print(item)
