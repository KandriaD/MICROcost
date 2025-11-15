import sys
import pandas as pd
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

