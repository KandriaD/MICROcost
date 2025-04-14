import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Ensure the Libraries folder is in sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
libraries_path = os.path.join(script_dir, "..", "Libraries")
if libraries_path not in sys.path:
    sys.path.append(libraries_path)

# Import custom libraries
import bacteria
import media
import courseinfo
import supplies
import antibiotics
import chemicals

# Global storage variables
added_biologicals = []
added_supplies = []
added_uninoculated_media = []
added_chemicals = []

# Function to update preview
def update_preview():
    preview_text.config(state="normal")
    preview_text.delete(1.0, tk.END)

    preview_text.insert(tk.END, f"=== Biologicals ===\n")
    for b in added_biologicals:
        preview_text.insert(tk.END, f"{b['specimen']} on {b['media']} ({b['type']}) [{b['distribution']}]: ${b['cost']}\n")

    preview_text.insert(tk.END, f"\n=== Supplies ===\n")
    for s in added_supplies:
        preview_text.insert(tk.END, f"{s['name']} [{s['distribution']}]: ${s['cost']}\n")

    preview_text.insert(tk.END, f"\n=== Uninoculated Media ===\n")
    for m in added_uninoculated_media:
        preview_text.insert(tk.END, f"{m['media']} ({m['type']}) [{m['distribution']}]: ${m['cost']}\n")

    preview_text.insert(tk.END, f"\n=== Chemicals ===\n")
    for c in added_chemicals:
        preview_text.insert(tk.END, f"{c['chemical']} ({c['type']}) [{c['distribution']}]: ${c['cost']}\n")
    
    total_bio_cost = sum(b['cost'] for b in added_biologicals)
    total_supply_cost = sum(s['cost'] for s in added_supplies)
    total_media_cost = sum(m['cost'] for m in added_uninoculated_media)
    total_chemical_cost = sum(c['cost'] for c in added_chemicals)

    preview_text.insert(tk.END, f"\nTotal Biological Cost: ${round(total_bio_cost, 2)}\n")
    preview_text.insert(tk.END, f"Total Supplies Cost: ${round(total_supply_cost, 2)}\n")
    preview_text.insert(tk.END, f"Total Media Cost: ${round(total_media_cost, 2)}\n")
    preview_text.insert(tk.END, f"Total Chemical Cost: ${round(total_chemical_cost, 2)}\n")
    preview_text.insert(tk.END, f"Grand Total: ${round(total_bio_cost + total_supply_cost + total_media_cost + total_chemical_cost, 2)}\n")

    preview_text.config(state="disabled")

# Function to remove last biological
def remove_last_biological():
    if added_biologicals:
        removed = added_biologicals.pop()
        print(f"Removed biological: {removed['specimen']}")
        update_preview()

# Function to remove last supply
def remove_last_supply():
    if added_supplies:
        removed = added_supplies.pop()
        print(f"Removed supply: {removed['name']}")
        update_preview()

# Function to remove last uninoculated media
def remove_last_uninoculated_media():
    if added_uninoculated_media:
        removed = added_uninoculated_media.pop()
        print(f"Removed uninoculated media: {removed['media']}")
        update_preview()

# Function to remove last chemical
def remove_last_chemical():
    if added_chemicals:
        removed = added_chemicals.pop()
        print(f"Removed chemical: {removed['chemical']}")
        update_preview()

# Function to clear all inputs
def clear_inputs():
    specimen_var.set("")
    media_var.set("")
    type_var.set("")
    distribution_entry.delete(0, tk.END)
    distribution_type_var.set("")
    supply_var.set("")
    supply_quantity_entry.delete(0, tk.END)
    supply_quantity_type_var.set("")
    media_uninoc_var.set("")
    media_uninoc_type_var.set("")
    media_uninoc_quantity_entry.delete(0, tk.END)
    media_uninoc_quantity_type_var.set("")
    chemical_var.set("")
    chemical_type_var.set("")
    chemical_quantity_entry.delete(0, tk.END)
    chemical_quantity_type_var.set("")

# Function to add biological
def add_biological():
    selected_specimen = specimen_var.get()
    selected_media = media_var.get()
    selected_type = type_var.get()
    dist_num = distribution_entry.get()
    dist_type = distribution_type_var.get()

    if not all([selected_specimen, selected_media, selected_type, dist_num, dist_type]):
        print("Missing info for biological")
        return

    try:
        dist_num = int(dist_num)
    except ValueError:
        print("Distribution quantity must be a number")
        return

    course = courseinfo.courses.get(course_type_var.get())
    if not course:
        print("No course selected or invalid")
        return

    volume_ml = media.standard_volumes_ml[selected_type]
    media_data = next((v for k, v in media.media_list.items() if v["name"] == selected_media), None)

    if not media_data:
        print(f"No media data found for {selected_media}")
        return

    cost_per_ml = media_data["cost_per_ml"]
    total_samples = {
        "Per Student": course.students,
        "Per Group": course.groups,
        "Per Section": course.sections,
        "Per Table": 6 * course.sections,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    added_biologicals.append({
        "specimen": selected_specimen,
        "media": selected_media,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added biological: {selected_specimen}, Cost: ${round(total_cost, 2)}")
    update_preview()

# Function to add supply
def add_supply():
    selected_supply = supply_var.get()
    quantity = supply_quantity_entry.get()
    quantity_type = supply_quantity_type_var.get()

    if not all([selected_supply, quantity, quantity_type]):
        print("Missing supply info")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        print("Quantity must be a number")
        return

    course = courseinfo.courses.get(course_type_var.get())
    if not course:
        print("Invalid course selection")
        return

    supply_info = supplies.general_supplies.get(selected_supply)
    if not supply_info:
        print("Supply not found")
        return

    per_item_cost = supply_info["cost_per_unit"]
    total_units = {
        "Per Student": course.students,
        "Per Group": course.groups,
        "Per Section": course.sections,
        "Per Table": 6 * course.sections,
    }.get(quantity_type, 1) * quantity

    total_cost = total_units * per_item_cost

    added_supplies.append({
        "name": selected_supply,
        "distribution": f"{quantity} {quantity_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added supply: {selected_supply}, Cost: ${round(total_cost, 2)}")
    update_preview()

# Function to add uninoculated media
def add_uninoculated_media():
    selected_media = media_uninoc_var.get()
    selected_type = media_uninoc_type_var.get()
    dist_num = media_uninoc_quantity_entry.get()
    dist_type = media_uninoc_quantity_type_var.get()

    if not all([selected_media, selected_type, dist_num, dist_type]):
        print("Missing info for media")
        return

    try:
        dist_num = int(dist_num)
    except ValueError:
        print("Distribution quantity must be a number")
        return

    course = courseinfo.courses.get(course_type_var.get())
    if not course:
        print("No course selected or invalid")
        return

    volume_ml = media.standard_volumes_ml[selected_type]
    media_data = next((v for k, v in media.media_list.items() if v["name"] == selected_media), None)

    if not media_data:
        print(f"No media data found for {selected_media}")
        return

    cost_per_ml = media_data["cost_per_ml"]
    total_samples = {
        "Per Student": course.students,
        "Per Group": course.groups,
        "Per Section": course.sections,
        "Per Table": 6 * course.sections,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    added_uninoculated_media.append({
        "media": selected_media,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added uninoculated media: {selected_media}, Cost: ${round(total_cost, 2)}")
    update_preview()

# Function to add chemical
def add_chemical():
    selected_chemical = chemical_var.get()
    selected_type = chemical_type_var.get()
    dist_num = chemical_quantity_entry.get()
    dist_type = chemical_quantity_type_var.get()

    if not all([selected_chemical, selected_type, dist_num, dist_type]):
        print("Missing info for chemical")
        return

    try:
        dist_num = int(dist_num)
    except ValueError:
        print("Distribution quantity must be a number")
        return

    course = courseinfo.courses.get(course_type_var.get())
    if not course:
        print("No course selected or invalid")
        return

    volume_ml = media.standard_volumes_ml[selected_type]
    chemical_data = chemicals.chemicals.get(selected_chemical)

    if not chemical_data:
        print(f"No chemical data found for {selected_chemical}")
        return

    cost_per_ml = chemical_data["cost_per_ml"]
    total_samples = {
        "Per Student": course.students,
        "Per Group": course.groups,
        "Per Section": course.sections,
        "Per Table": 6 * course.sections,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    added_chemicals.append({
        "chemical": selected_chemical,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added chemical: {selected_chemical}, Cost: ${round(total_cost, 2)}")
    update_preview()

# --- GUI Layout Setup ---
root = tk.Tk()
root.title("Microbiology Lab Cost Calculator")

# Scrollable Frame Setup
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ttk.Frame(canvas)

# Add scrollable_frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

scrollbar.grid(row=0, column=1, sticky="ns")
canvas.grid(row=0, column=0, sticky="nsew")

# Configure the scroll region to the size of the scrollable_frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Input fields, buttons, and frames for biologicals, supplies, and other data
frame = ttk.Frame(scrollable_frame)
frame.grid(row=0, column=0, padx=10, pady=10)

specimen_label = ttk.Label(frame, text="Specimen:")
specimen_label.grid(row=0, column=0, sticky="w")

specimen_var = tk.StringVar()
specimen_entry = ttk.Entry(frame, textvariable=specimen_var)
specimen_entry.grid(row=0, column=1)

media_label = ttk.Label(frame, text="Media:")
media_label.grid(row=1, column=0, sticky="w")

media_var = tk.StringVar()
media_menu = ttk.Combobox(frame, textvariable=media_var, values=list(media.media_list.keys()))
media_menu.grid(row=1, column=1)

type_label = ttk.Label(frame, text="Type:")
type_label.grid(row=2, column=0, sticky="w")

type_var = tk.StringVar()
type_menu = ttk.Combobox(frame, textvariable=type_var, values=list(media.standard_volumes_ml.keys()))
type_menu.grid(row=2, column=1)

distribution_label = ttk.Label(frame, text="Distribution Quantity:")
distribution_label.grid(row=3, column=0, sticky="w")

distribution_entry = ttk.Entry(frame)
distribution_entry.grid(row=3, column=1)

distribution_type_var = tk.StringVar()
distribution_type_menu = ttk.Combobox(frame, textvariable=distribution_type_var, values=["Per Student", "Per Group", "Per Section", "Per Table"])
distribution_type_menu.grid(row=4, column=1)

add_biological_button = ttk.Button(frame, text="Add Biological", command=add_biological)
add_biological_button.grid(row=5, column=0, pady=10)

remove_biological_button = ttk.Button(frame, text="Remove Last Biological", command=remove_last_biological)
remove_biological_button.grid(row=5, column=1, pady=10)

# Course Info
course_frame = ttk.LabelFrame(frame, text="Course Info")
course_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

ttk.Label(course_frame, text="Course Name").grid(row=0, column=0, padx=5, pady=5)
course_type_var = tk.StringVar()
course_type_dropdown = ttk.Combobox(course_frame, textvariable=course_type_var, values=list(courseinfo.courses.keys()))
course_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Experiment Name
ttk.Label(frame, text="Experiment Name:").grid(row=1, column=0, padx=5, pady=5)
experiment_name = ttk.Entry(frame, width=40)
experiment_name.grid(row=1, column=1, padx=5, pady=5)

# Supplies Section
supply_label = ttk.Label(frame, text="Supply:")
supply_label.grid(row=6, column=0, sticky="w")

supply_var = tk.StringVar()
supply_menu = ttk.Combobox(frame, textvariable=supply_var, values=list(supplies.general_supplies.keys()))
supply_menu.grid(row=6, column=1)

supply_quantity_label = ttk.Label(frame, text="Quantity:")
supply_quantity_label.grid(row=7, column=0, sticky="w")

supply_quantity_entry = ttk.Entry(frame)
supply_quantity_entry.grid(row=7, column=1)

supply_quantity_type_var = tk.StringVar()
supply_quantity_type_menu = ttk.Combobox(frame, textvariable=supply_quantity_type_var, values=["Per Student", "Per Group", "Per Section", "Per Table"])
supply_quantity_type_menu.grid(row=8, column=1)

add_supply_button = ttk.Button(frame, text="Add Supply", command=add_supply)
add_supply_button.grid(row=9, column=0, pady=10)

remove_supply_button = ttk.Button(frame, text="Remove Last Supply", command=remove_last_supply)
remove_supply_button.grid(row=9, column=1, pady=10)

# Uninoculated Media Section
media_uninoc_label = ttk.Label(frame, text="Uninoculated Media:")
media_uninoc_label.grid(row=10, column=0, sticky="w")

media_uninoc_var = tk.StringVar()
media_uninoc_menu = ttk.Combobox(frame, textvariable=media_uninoc_var, values=list(media.media_list.keys()))
media_uninoc_menu.grid(row=10, column=1)

media_uninoc_type_label = ttk.Label(frame, text="Type:")
media_uninoc_type_label.grid(row=11, column=0, sticky="w")

media_uninoc_type_var = tk.StringVar()
media_uninoc_type_menu = ttk.Combobox(frame, textvariable=media_uninoc_type_var, values=list(media.standard_volumes_ml.keys()))
media_uninoc_type_menu.grid(row=11, column=1)

media_uninoc_quantity_label = ttk.Label(frame, text="Quantity:")
media_uninoc_quantity_label.grid(row=12, column=0, sticky="w")

media_uninoc_quantity_entry = ttk.Entry(frame)
media_uninoc_quantity_entry.grid(row=12, column=1)

media_uninoc_quantity_type_var = tk.StringVar()
media_uninoc_quantity_type_menu = ttk.Combobox(frame, textvariable=media_uninoc_quantity_type_var, values=["Per Student", "Per Group", "Per Section", "Per Table"])
media_uninoc_quantity_type_menu.grid(row=13, column=1)

add_uninoculated_media_button = ttk.Button(frame, text="Add Uninoculated Media", command=add_uninoculated_media)
add_uninoculated_media_button.grid(row=14, column=0, pady=10)

remove_uninoculated_media_button = ttk.Button(frame, text="Remove Last Uninoculated Media", command=remove_last_chemical)
remove_uninoculated_media_button.grid(row=14, column=1, pady=10)

# Chemical Section
chemical_label = ttk.Label(frame, text="Chemical:")
chemical_label.grid(row=15, column=0, sticky="w")

chemical_var = tk.StringVar()
chemical_menu = ttk.Combobox(frame, textvariable=chemical_var, values=list(chemicals.chemicals.keys()))
chemical_menu.grid(row=15, column=1)

chemical_type_label = ttk.Label(frame, text="Type:")
chemical_type_label.grid(row=16, column=0, sticky="w")

chemical_type_var = tk.StringVar()
chemical_type_menu = ttk.Combobox(frame, textvariable=chemical_type_var, values=list(media.standard_volumes_ml.keys()))
chemical_type_menu.grid(row=16, column=1)

chemical_quantity_label = ttk.Label(frame, text="Quantity:")
chemical_quantity_label.grid(row=17, column=0, sticky="w")

chemical_quantity_entry = ttk.Entry(frame)
chemical_quantity_entry.grid(row=17, column=1)

chemical_quantity_type_var = tk.StringVar()
chemical_quantity_type_menu = ttk.Combobox(frame, textvariable=chemical_quantity_type_var, values=["Per Student", "Per Group", "Per Section", "Per Table"])
chemical_quantity_type_menu.grid(row=18, column=1)

add_chemical_button = ttk.Button(frame, text="Add Chemical", command=add_chemical)
add_chemical_button.grid(row=19, column=0, pady=10)

remove_chemical_button = ttk.Button(frame, text="Remove Last Chemical", command=remove_last_chemical)
remove_chemical_button.grid(row=19, column=1, pady=10)# Preview Frame
preview_frame = ttk.Frame(scrollable_frame)
preview_frame.grid(row=1, column=0, padx=10, pady=10)

preview_text = tk.Text(preview_frame, wrap="none", width=60, height=20)
preview_text.grid(row=0, column=0)

export_button = ttk.Button(scrollable_frame, text="Export Summary", command=update_preview)
export_button.grid(row=2, column=0, pady=20)

clear_button = ttk.Button(scrollable_frame, text="Clear All Inputs", command=clear_inputs)
clear_button.grid(row=3, column=0, pady=10)

root.mainloop()