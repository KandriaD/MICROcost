# Import libraries
import sys
sys.path.append(r'C:\Users\Kandriad\Documents\GitHub\MICROcost\Libraries')

import antibiotics
import bacteria
import chemicals
import media
import supplies

#import tkinter for user interface display
import tkinter as tk
from tkinter import ttk

def calculate_cost():
    pass

def add_biological():
    pass

def add_supply():
    pass

# Initialize main window
root = tk.Tk()
root.title("Microbiology Lab Cost Calculator")
root.geometry("600x900")

# Experiment Name
ttk.Label(root, text="Experiment Name:").grid(row=0, column=0, padx=5, pady=5)
experiment_name = ttk.Entry(root, width=40)
experiment_name.grid(row=0, column=1, padx=5, pady=5)

# **Course Info Section**
course_frame = ttk.LabelFrame(root, text="Course Info")  # Frame for course information
course_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")  # Ensure proper grid placement

# Labels and Entry Fields inside course_frame
ttk.Label(course_frame, text="Course Number").grid(row=0, column=0, padx=5, pady=5)
course_entry = ttk.Entry(course_frame, width=10)
course_entry.grid(row=0, column=1, padx=5, pady=5)
course_type_var = tk.StringVar()
course_type_dropdown = ttk.Combobox(course_entry, values=["MICRO 140L", "MICRO 351L", "MICRO 401L", "MICRO 461L", "MICRO 463L"])
course_type_dropdown.grid(row=2, column=1, padx=5, pady=5)

##########try to pull this info from courseinfo.py

#ttk.Label(course_frame, text="Number of Sections").grid(row=1, column=0, padx=5, pady=5)
#sections_entry = ttk.Entry(course_frame, width=10)
#sections_entry.grid(row=1, column=1, padx=5, pady=5)

#ttk.Label(course_frame, text="Number of Students").grid(row=2, column=0, padx=5, pady=5)
#students_entry = ttk.Entry(course_frame, width=10)
#students_entry.grid(row=2, column=1, padx=5, pady=5)

#ttk.Label(course_frame, text="Number of Groups").grid(row=3, column=0, padx=5, pady=5)
#groups_entry = ttk.Entry(course_frame, width=10)
#groups_entry.grid(row=3, column=1, padx=5, pady=5)

# **Biologicals Section**
bio_frame = ttk.LabelFrame(root, text="Biologicals")
bio_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

ttk.Label(bio_frame, text="Specimen:").grid(row=0, column=0, padx=5, pady=5)
specimen_var = tk.StringVar()
specimen_dropdown = ttk.Combobox(bio_frame, textvariable=specimen_var)
specimen_dropdown.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(bio_frame, text="Media:").grid(row=1, column=0, padx=5, pady=5)
media_var = tk.StringVar()
media_dropdown = ttk.Combobox(bio_frame, textvariable=media_var)
media_dropdown.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(bio_frame, text="Distribution:").grid(row=2, column=0, padx=5, pady=5)
distribution_var = tk.StringVar()
distribution_dropdown = ttk.Combobox(bio_frame, textvariable=distribution_var, values=["Plate", "Slant", "Deep", "Premade", "Microcentrifuge Tube"])
distribution_dropdown.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(bio_frame, text="Quantity:").grid(row=3, column=0, padx=5, pady=5)
quantity_entry = ttk.Entry(bio_frame, width=10)
quantity_entry.grid(row=3, column=1, padx=5, pady=5)
quantity_type_var = tk.StringVar()
quantity_type_dropdown = ttk.Combobox(bio_frame, textvariable=quantity_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
quantity_type_dropdown.grid(row=3, column=2, padx=5, pady=5)

add_bio_button = ttk.Button(bio_frame, text="Add Biological", command=add_biological)
add_bio_button.grid(row=4, column=0, columnspan=3, pady=5)

# **Supplies Section**
supplies_frame = ttk.LabelFrame(root, text="Supplies")
supplies_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

ttk.Label(supplies_frame, text="Supply:").grid(row=0, column=0, padx=5, pady=5)
supply_var = tk.StringVar()
supply_dropdown = ttk.Combobox(supplies_frame, textvariable=supply_var)
supply_dropdown.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(supplies_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
supply_quantity_entry = ttk.Entry(supplies_frame, width=10)
supply_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
supply_quantity_type_var = tk.StringVar()
supply_quantity_type_dropdown = ttk.Combobox(supplies_frame, textvariable=quantity_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
supply_quantity_type_dropdown.grid(row=1, column=2, padx=5, pady=5)

add_supply_button = ttk.Button(supplies_frame, text="Add Supply", command=add_supply)
add_supply_button.grid(row=2, column=0, columnspan=2, pady=5)

# **Results Section**
results_frame = ttk.LabelFrame(root, text="Selected Items")
results_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
results_list = tk.Listbox(results_frame, width=80, height=10)
results_list.pack(padx=5, pady=5)

# **Calculate Cost Button**
calculate_button = ttk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
