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

# Uninoculated Media Section
media_uninoc_frame = ttk.LabelFrame(input_frame, text="Uninoculated Media")
media_uninoc_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

media_uninoc_var = tk.StringVar()
media_uninoc_dropdown = ttk.Combobox(media_uninoc_frame, textvariable=media_uninoc_var, state="readonly", width=40)
media_uninoc_dropdown.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(media_uninoc_frame, text="Media:").grid(row=0, column=0, padx=5, pady=5)

media_uninoc_type_var = tk.StringVar()
media_uninoc_type_dropdown = ttk.Combobox(media_uninoc_frame, textvariable=media_uninoc_type_var, state="readonly", width=25)
media_uninoc_type_dropdown.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(media_uninoc_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)

media_uninoc_quantity_entry = ttk.Entry(media_uninoc_frame, width=10)
media_uninoc_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
media_uninoc_quantity_type_var = tk.StringVar()
media_uninoc_quantity_type_dropdown = ttk.Combobox(media_uninoc_frame, textvariable=media_uninoc_quantity_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
media_uninoc_quantity_type_dropdown.grid(row=2, column=2, padx=5, pady=5)
ttk.Label(media_uninoc_frame, text="Distribution:").grid(row=2, column=0, padx=5, pady=5)

media_uninoc_dropdown.bind("<<ComboboxSelected>>", lambda event: media_uninoc_type_dropdown.config(values=list(media.standard_volumes_ml.keys())))
add_media_button = ttk.Button(media_uninoc_frame, text="Add Media", command=add_uninoculated_media)
add_media_button.grid(row=3, column=0, columnspan=3, pady=5)

# Chemicals Section
chemicals_frame = ttk.LabelFrame(input_frame, text="Chemicals")
chemicals_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

chemical_var = tk.StringVar()
chemical_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_var, state="readonly", width=40)
chemical_dropdown.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Chemical:").grid(row=0, column=0, padx=5, pady=5)

chemical_type_var = tk.StringVar()
chemical_type_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_type_var, state="readonly", width=25)
chemical_type_dropdown.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)

chemical_quantity_entry = ttk.Entry(chemicals_frame, width=10)
chemical_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
chemical_quantity_type_var = tk.StringVar()
chemical_quantity_type_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_quantity_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
chemical_quantity_type_dropdown.grid(row=2, column=2, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Distribution:").grid(row=2, column=0, padx=5, pady=5)

chemical_dropdown.bind("<<ComboboxSelected>>", lambda event: chemical_type_dropdown.config(values=list(media.standard_volumes_ml.keys())))
add_chemical_button = ttk.Button(chemicals_frame, text="Add Chemical", command=add_chemical)
add_chemical_button.grid(row=3, column=0, columnspan=3, pady=5)

# Populate Dropdowns
if hasattr(media, "media_list"):
    media_uninoc_dropdown["values"] = [value["name"] for key, value in media.media_list.items()]
if hasattr(chemicals, "chemicals"):
    chemical_dropdown["values"] = list(chemicals.chemicals.keys())
