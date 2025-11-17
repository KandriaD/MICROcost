import sys
import pandas as pd
import glob
import os
from openpyxl import load_workbook
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_COLOR_INDEX, WD_ALIGN_PARAGRAPH

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

def load_course_info(course_df):
    return {
        "students":int(course_df.loc[0, "Students"]),
        "sections":int(course_df.loc[0, "Sections"]),
        "groups":int(course_df.loc[0, "Groups"]),
        "rooms": course_df.loc[0, "Rooms"].split(",")
    }

def calculate_total_qty(quantity, dist_type, course_info, form=None):
    multiplier = {
        "Per Student": course_info["students"],
        "Per Group": course_info["groups"],\
        "Per Section": course_info["sections"],
        "Per Table": sum(5 if room.strip() == "113" else 6 for room in course_info['rooms']),
        "Per Room": len(course_info["rooms"]),
        "Per Course": 1
    }.get(dist_type, 1)
    
    return quantity * multiplier #special forms shouldnt matter here because the end goal is cost, not how many samples to prepare

def lookup_by_name_or_key(name, library_dict, lib_label="item"):
    if not name or str(name).lower() == "nan":
        return None
    name_lower = str(name).strip().lower()

    for key, info in library_dict.items():
        if key.strip().lower() == name_lower:
            return info
        
        if str(info.get("name", "")).strip().lower() == name_lower:
            return info
        
        synonyms = info.get("synonym" or "synonyms", [])
        if any(syn.strip().lower == name_lower for syn in synonyms):
            return info
        
    print(f"Warning: '{name}' not found in {lib_label} library")
    return None

def is_valid_bacteria(name):
    return lookup_by_name_or_key(name, bacteria.bacteria_list, "bacteria") is not None
def is_valid_media(name):
    return lookup_by_name_or_key(name, media.media_list, "media") is not None
def is_valid_supply(name):
    return lookup_by_name_or_key(name, supplies.supplies, "supply") is not None
def is_valid_chemical(name):
    return lookup_by_name_or_key(name, chemicals.chemical_list, "chemical") is not None
def is_valid_antibiotic(name):
    return lookup_by_name_or_key(name, antibiotics.antibiotics, "antibiotic") is not None

def validate_item(name, category):
    if category == "Biological":
        return is_valid_bacteria(name)
    elif category == "Uninoculated Media":
        return is_valid_media
    elif category == "Chemical":
        return is_valid_chemical
    elif category == "Supply":
        return is_valid_supply
    elif category == "Antibiotics":
        return is_valid_antibiotic

def gather_all_items(course_name=None): ##doesnt have cost stuff in it yet, just pulling from doc 

    folder_path = r"C:\Kandriad\Desktop\ExpFiles"
    pattern = os.path.join(folder_path, "*Expeeriments.xlsx")
    experiment_files = glob.glob(pattern)

    for file in experiment_files:
        course_name = os.path.bsename(file).split("Experiments.xlsx")[0]
        xls = pd.ExcelFile(file)
        course_df = xls.parse("CourseInfo")
        course_info = load_course_info(course_df)

    experiment_list_df = xls.parse("ExperimentIndex")
    experiment_list_df.columns = experiment_list_df.columns.str.strip()

    for _, row in experiment_list_df.iterrows():
        exp_title = row["Experiment Title"]
        sheet_name = str(row["SheetName"])
        if sheet_name.endswith(".0"):
            sheet_name = sheet_name[:-2]

        if sheet_name not in xls.sheet_names:
            print(f"Sheet '{sheet_name}' not found in file '{file}' -- Skipping.")
            continue

    experiment_df = xls.parse(experiment_list_df)
    experiment_df.columns = experiment_df.columns.str.strip()

    for _, item in experiment_df.iterrows():
        item_category = str(item.get("Category", "")).stip()
        if not item_category or item_category.lower() == "nan":
            continue

        item_name = item.get("Item/Organism")

        if pd.isna(item_name) and item_category == "Uninoculated Media":
            item_name == item.get("Media Used")
            name = str(item_name).strip() if not pd.isna(item_name) else ""
            media_used = item.get("Media Used", 0)
            form = item.get("Form", 0)
            quantity = item.get("Quantity", 0)
            dist_type = str(item.get("DistributionType", "")).strip().title()

            try:
                total_qty = calculate_total_qty(quantity, dist_type, course_info, form)
            except Exception as e:
                print(f"Error calculating quantity for {course_name} {exp_title} - {item_category} {name} {media_used}: {e}")
                continue

