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

    total_bio_cost = sum(b['cost'] for b in added_biologicals)
    total_supply_cost = sum(s['cost'] for s in added_supplies)

    preview_text.insert(tk.END, f"\nTotal Biological Cost: ${round(total_bio_cost, 2)}\n")
    preview_text.insert(tk.END, f"Total Supplies Cost: ${round(total_supply_cost, 2)}\n")
    preview_text.insert(tk.END, f"Grand Total: ${round(total_bio_cost + total_supply_cost, 2)}\n")

    preview_text.config(state="disabled")

# Function to calculate cost (currently empty, can be filled later)
def calculate_cost():
    pass

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
        "Per Table": 6 * course.sections,  # Approximation
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
    update_preview()  # Call after adding biological

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
    update_preview()  # Call after adding supply

# Initialize main window
root = tk.Tk()
root.title("Microbiology Lab Cost Calculator")
root.geometry("600x900")

# Experiment Name
ttk.Label(root, text="Experiment Name:").grid(row=0, column=0, padx=5, pady=5)
experiment_name = ttk.Entry(root, width=40)
experiment_name.grid(row=0, column=1, padx=5, pady=5)

# **Course Info Section**
course_frame = ttk.LabelFrame(root, text="Course Info")
course_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Course Dropdown
ttk.Label(course_frame, text="Course Name").grid(row=0, column=0, padx=5, pady=5)
course_type_var = tk.StringVar()
course_type_dropdown = ttk.Combobox(course_frame, textvariable=course_type_var, values=list(courseinfo.courses.keys()))
course_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# **Biologicals Section**
bio_frame = ttk.LabelFrame(root, text="Biologicals")
bio_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Specimen Dropdown
ttk.Label(bio_frame, text="Specimen:").grid(row=0, column=0, padx=5, pady=5)
specimen_var = tk.StringVar()
specimen_dropdown = ttk.Combobox(bio_frame, textvariable=specimen_var, state="readonly", width=30)
specimen_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Media Dropdown
ttk.Label(bio_frame, text="Media:").grid(row=1, column=0, padx=5, pady=5)
media_var = tk.StringVar()
media_dropdown = ttk.Combobox(bio_frame, textvariable=media_var, state="readonly", width=40)
media_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Type Dropdown (formerly Distribution)
ttk.Label(bio_frame, text="Type:").grid(row=2, column=0, padx=5, pady=5)
type_var = tk.StringVar()
type_dropdown = ttk.Combobox(bio_frame, textvariable=type_var, state="readonly", width=25)
type_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Distribution Input (Numeric + Type Dropdown)
ttk.Label(bio_frame, text="Distribution:").grid(row=3, column=0, padx=5, pady=5)
distribution_entry = ttk.Entry(bio_frame, width=10)
distribution_entry.grid(row=3, column=1, padx=5, pady=5)
distribution_type_var = tk.StringVar()
distribution_type_dropdown = ttk.Combobox(bio_frame, textvariable=distribution_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
distribution_type_dropdown.grid(row=3, column=2, padx=5, pady=5)

# Function to update Type options based on Media selection
def update_type_options(event):
    selected_media = media_var.get()
    if selected_media and hasattr(media, "standard_volumes_ml"):
        type_dropdown["values"] = list(media.standard_volumes_ml.keys())
        type_dropdown.set("Select a type")
    else:
        print("Error: No valid media selected or media data not available.")

media_dropdown.bind("<<ComboboxSelected>>", update_type_options)

# Populate Dropdowns
try:
    if hasattr(bacteria, "bacteria_list"):
        specimen_dropdown["values"] = list(bacteria.bacteria_list)
    else:
        print("Error: 'bacteria_list' not found in bacteria.py")

    if hasattr(media, "media_list"):
        media_dropdown["values"] = [value["name"] for key, value in media.media_list.items()]
    else:
        print("Error: 'media_list' not found in media.py")
except AttributeError as e:
    print(f"Error populating dropdowns: {e}")

add_biological_button = ttk.Button(bio_frame, text="Add Biological", command=add_biological)
add_biological_button.grid(row=4, column=0, columnspan=3, pady=5)

# **Supplies Section**
supplies_frame = ttk.LabelFrame(root, text="Supplies")
supplies_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# General Supply Dropdown
ttk.Label(supplies_frame, text="Supply:").grid(row=0, column=0, padx=5, pady=5)
supply_var = tk.StringVar()
supply_dropdown = ttk.Combobox(supplies_frame, textvariable=supply_var, state="readonly", width=40)
supply_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Quantity Input
ttk.Label(supplies_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
supply_quantity_entry = ttk.Entry(supplies_frame, width=10)
supply_quantity_entry.grid(row=1, column=1, padx=5, pady=5)

# Quantity Type Dropdown
ttk.Label(supplies_frame, text="Quantity Type:").grid(row=1, column=2, padx=5, pady=5)
supply_quantity_type_var = tk.StringVar()
quantity_type_dropdown = ttk.Combobox(supplies_frame, textvariable=supply_quantity_type_var, values=["Per Section", "Per Table", "Per Group", "Per Student"])
quantity_type_dropdown.grid(row=1, column=3, padx=5, pady=5)

# Add Supply Button
add_supply_button = ttk.Button(supplies_frame, text="Add Supply", command=add_supply)
add_supply_button.grid(row=2, column=0, columnspan=4, pady=5)

# **Preview Section**
preview_frame = ttk.LabelFrame(root, text="Preview")
preview_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Preview Textbox
preview_text = tk.Text(preview_frame, width=70, height=15, state="disabled", wrap="word")
preview_text.pack(padx=5, pady=5)

# Start the main GUI loop
root.mainloop()
