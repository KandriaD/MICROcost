import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
import csv

# --- Define global variables for muliple experiments ---
experiments = {}  # Dictionary to store all experiment data
current_experiment = None  # Variable to store the name of the current experiment
biologicals_list = []  # List to store biologicals for the current experiment
supplies_list = []  # List to store supplies for the current experiment
media_list = []  # List to store media for the current experiment
chemicals_list = []  # List to store chemicals for the current experiment

# --- Ensure the Libraries folder is in sys.path ---
script_dir = os.path.dirname(os.path.abspath(__file__))
libraries_path = os.path.join(script_dir, "..", "Libraries")
if libraries_path not in sys.path:
    sys.path.append(libraries_path)

# --- Import custom libraries ---
import bacteria
import media
import courseinfo
import supplies
import antibiotics
import chemicals

# --- Global storage variables for adding materials ---
added_biologicals = []
added_supplies = []
added_uninoculated_media = []
added_chemicals = []

# --- Funtion to start a new experiment ---
def start_new_experiment():
    global current_experiment
    
    # Set the current experiment to a new name (you may already have a method to get this)
    experiment_name = experiment_name_entry.get()  # or use another variable
    current_experiment = experiment_name  # Ensure it's assigned here

    # Initialize the lists for the new experiment
    global biologicals_list, supplies_list, media_list, chemicals_list
    biologicals_list = []
    supplies_list = []
    media_list = []
    chemicals_list = []

    print(f"Started new experiment: {current_experiment}")

# --- Functions for updating preview and adding/removing items ---
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

# --- Functions to add and remove biologicals, supplies, uninoculated media, and chemicals ---
def remove_last_biological():
    if added_biologicals:
        removed = added_biologicals.pop()
        print(f"Removed biological: {removed['specimen']}")
        update_preview()

def remove_last_supply():
    if added_supplies:
        removed = added_supplies.pop()
        print(f"Removed supply: {removed['name']}")
        update_preview()

def remove_last_uninoculated_media():
    if added_uninoculated_media:
        removed = added_uninoculated_media.pop()
        print(f"Removed uninoculated media: {removed['media']}")
        update_preview()

def remove_last_chemical():
    if added_chemicals:
        removed = added_chemicals.pop()
        print(f"Removed chemical: {removed['chemical']}")
        update_preview()

def add_biological():
    global biologicals_list

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
        "Per Pair": course.students // 2,
        "Per Group": course.groups,
        "Per Table": 6 * course.sections,
        "Per Section": course.sections,
        "Per Room": len(course.rooms),
        "Per Course": 1,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    biological = {
        "specimen": selected_specimen,
        "media": selected_media,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    }

    biologicals_list.append(biological)

    added_biologicals.append(biological)

    print(f"Added biological: {selected_specimen}, Cost: ${round(total_cost, 2)}")
    update_preview()

def add_supply():
    global supplies_list

    selected_supply_name = supply_var.get()
    quantity = supply_quantity_entry.get()
    quantity_type = supply_quantity_type_var.get()

    if not all([selected_supply_name, quantity, quantity_type]):
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

    # Get the key using the name-to-key dictionary
    supply_key = supply_name_to_key.get(selected_supply_name)
    if not supply_key:
        print("Supply key not found")
        return

    supply_info = supplies.supplies.get(supply_key)
    if not supply_info:
        print("Supply info not found")
        return

    per_item_cost = supply_info["cost_per_unit"] / supply_info["quantity"]
    units = {
        "Per Student": course.students,
        "Per Pair": course.students // 2,
        "Per Group": course.groups,
        "Per Table": 6 * course.sections,
        "Per Section": course.sections,
        "Per Room": len(course.rooms),
        "Per Course": 1,
    }.get(quantity_type, 1) * quantity

    total_cost = units * per_item_cost

    supplies_list.append({
        "name": selected_supply_name,
        "distribution": f"{quantity} {quantity_type}",
        "cost": round(total_cost, 2)
    })

    added_supplies.append({
        "name": selected_supply_name,
        "distribution": f"{quantity} {quantity_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added supply: {selected_supply_name}, Cost: ${round(total_cost, 2)}")
    update_preview()

def add_uninoculated_media():
    global media_list

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
        "Per Pair": course.students // 2,
        "Per Group": course.groups,
        "Per Table": 6 * course.sections,
        "Per Section": course.sections,
        "Per Room": len(course.rooms),
        "Per Course": 1,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    media_list.append({
        "media": selected_media,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

    added_uninoculated_media.append({
        "media": selected_media,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

    print(f"Added uninoculated media: {selected_media}, Cost: ${round(total_cost, 2)}")
    update_preview()

def add_chemical():
    global chemicals_list

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
        "Per Pair": course.students // 2,
        "Per Group": course.groups,
        "Per Table": 6 * course.sections,
        "Per Section": course.sections,
        "Per Room": len(course.rooms),
        "Per Course": 1,
    }.get(dist_type, 1) * dist_num

    total_cost = volume_ml * cost_per_ml * total_samples

    chemicals_list.append({
        "chemical": selected_chemical,
        "type": selected_type,
        "distribution": f"{dist_num} {dist_type}",
        "cost": round(total_cost, 2)
    })

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
root.geometry("1200x900")

# Layout Frames
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=0, column=0, sticky="nw")

preview_frame = ttk.LabelFrame(main_frame, text="Preview")
preview_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

# Course Info
course_frame = ttk.LabelFrame(input_frame, text="Course Info")
course_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

ttk.Label(course_frame, text="Course Name").grid(row=0, column=0, padx=5, pady=5)
course_type_var = tk.StringVar()
course_type_dropdown = ttk.Combobox(course_frame, textvariable=course_type_var, values=list(courseinfo.courses.keys()))
course_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Experiment Name (Label + Entry + Set Button using grid)
ttk.Label(input_frame, text="Experiment Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")

experiment_name_entry = ttk.Entry(input_frame, width=40)
experiment_name_entry.grid(row=1, column=1, padx=5, pady=5)

start_new_button = ttk.Button(input_frame, text="Set Experiment Name", command=start_new_experiment)
start_new_button.grid(row=1, column=2, padx=5, pady=5)

# Biologicals Section
bio_frame = ttk.LabelFrame(input_frame, text="Biologicals")
bio_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

specimen_var = tk.StringVar()
specimen_dropdown = ttk.Combobox(bio_frame, textvariable=specimen_var, state="readonly", width=30)
specimen_dropdown.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(bio_frame, text="Specimen:").grid(row=0, column=0, padx=5, pady=5)

media_var = tk.StringVar()
media_dropdown = ttk.Combobox(bio_frame, textvariable=media_var, state="readonly", width=40)
media_dropdown.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(bio_frame, text="Media:").grid(row=1, column=0, padx=5, pady=5)

type_var = tk.StringVar()
type_dropdown = ttk.Combobox(bio_frame, textvariable=type_var, state="readonly", width=25)
type_dropdown.grid(row=2, column=1, padx=5, pady=5)
ttk.Label(bio_frame, text="Type:").grid(row=2, column=0, padx=5, pady=5)

distribution_entry = ttk.Entry(bio_frame, width=10)
distribution_entry.grid(row=3, column=1, padx=5, pady=5)
distribution_type_var = tk.StringVar()
distribution_type_dropdown = ttk.Combobox(bio_frame, textvariable=distribution_type_var, values=["Per Course", "Per Room", "Per Section", "Per Table", "Per Group", "Per Pair", "Per Student"])
distribution_type_dropdown.grid(row=3, column=2, padx=5, pady=5)
ttk.Label(bio_frame, text="Distribution:").grid(row=3, column=0, padx=5, pady=5)

media_dropdown.bind("<<ComboboxSelected>>", lambda event: type_dropdown.config(values=list(media.standard_volumes_ml.keys())))

add_biological_button = ttk.Button(bio_frame, text="Add Biological", command=add_biological)
add_biological_button.grid(row=2, column=3, columnspan=3, pady=5)

remove_bio_button = ttk.Button(bio_frame, text="Remove Last Biological", command=remove_last_biological)
remove_bio_button.grid(row=3, column=3, columnspan=3, pady=5)

# Supplies Section
supplies_frame = ttk.LabelFrame(input_frame, text="Supplies")
supplies_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

supply_names = [item["name"] for item in supplies.supplies.values()]
supply_name_to_key = {item["name"]: key for key, item in supplies.supplies.items()}

supply_var = tk.StringVar()
supply_dropdown = ttk.Combobox(supplies_frame, textvariable=supply_var, values=supply_names, state="readonly", width=40)
supply_dropdown.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(supplies_frame, text="Supply:").grid(row=0, column=0, padx=5, pady=5)

supply_quantity_entry = ttk.Entry(supplies_frame, width=10)
supply_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(supplies_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)

supply_quantity_type_var = tk.StringVar()
quantity_type_dropdown = ttk.Combobox(supplies_frame, textvariable=supply_quantity_type_var, values=["Per Course", "Per Room", "Per Section", "Per Table", "Per Group", "Per Pair", "Per Student"])
quantity_type_dropdown.grid(row=1, column=3, padx=5, pady=5)
ttk.Label(supplies_frame, text="Quantity Type:").grid(row=1, column=2, padx=5, pady=5)

add_supply_button = ttk.Button(supplies_frame, text="Add Supply", command=add_supply)
add_supply_button.grid(row=0, column=4, columnspan=4, pady=5)

remove_supply_button = ttk.Button(supplies_frame, text="Remove Last Supply", command=remove_last_supply)
remove_supply_button.grid(row=1, column=4, columnspan=4, pady=5)

# Uninoculated Media Section
media_uninoc_frame = ttk.LabelFrame(input_frame, text="Uninoculated Media")
media_uninoc_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

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
media_uninoc_quantity_type_dropdown = ttk.Combobox(media_uninoc_frame, textvariable=media_uninoc_quantity_type_var, values=["Per Course", "Per Room", "Per Section", "Per Table", "Per Group", "Per Pair", "Per Student"])
media_uninoc_quantity_type_dropdown.grid(row=2, column=2, padx=5, pady=5)
ttk.Label(media_uninoc_frame, text="Distribution:").grid(row=2, column=0, padx=5, pady=5)

media_uninoc_dropdown.bind("<<ComboboxSelected>>", lambda event: media_uninoc_type_dropdown.config(values=list(media.standard_volumes_ml.keys())))
add_media_button = ttk.Button(media_uninoc_frame, text="Add Media", command=add_uninoculated_media)
add_media_button.grid(row=1, column=3, columnspan=3, pady=5)

remove_media_button = ttk.Button(media_uninoc_frame, text="Remove Last Media", command=remove_last_uninoculated_media)
remove_media_button.grid(row=2, column=3, columnspan=3, pady=5)

# Chemicals Section
chemicals_frame = ttk.LabelFrame(input_frame, text="Chemicals")
chemicals_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

chemical_key_to_name = {key: val["name"] for key, val in chemicals.chemical_list.items()}
chemical_name_to_key = {val["name"]: key for key, val in chemicals.chemical_list.items()}

chemical_var = tk.StringVar()
chemical_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_var, values=list(chemical_key_to_name.values()), state="readonly", width=40)
chemical_dropdown.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Chemical:").grid(row=0, column=0, padx=5, pady=5)

chemical_type_var = tk.StringVar()
chemical_type_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_type_var, state="readonly", width=25)
chemical_type_dropdown.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)

chemical_quantity_entry = ttk.Entry(chemicals_frame, width=10)
chemical_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
chemical_quantity_type_var = tk.StringVar()
chemical_quantity_type_dropdown = ttk.Combobox(chemicals_frame, textvariable=chemical_quantity_type_var, values=["Per Course", "Per Room", "Per Section", "Per Table", "Per Group", "Per Pair", "Per Student"])
chemical_quantity_type_dropdown.grid(row=2, column=2, padx=5, pady=5)
ttk.Label(chemicals_frame, text="Distribution:").grid(row=2, column=0, padx=5, pady=5)

chemical_dropdown.bind("<<ComboboxSelected>>", lambda event: chemical_type_dropdown.config(values=list(media.standard_volumes_ml.keys())))
add_chemical_button = ttk.Button(chemicals_frame, text="Add Chemical", command=add_chemical)
add_chemical_button.grid(row=3, column=0, columnspan=3, pady=5)

remove_chemical_button = ttk.Button(chemicals_frame, text="Remove Last Chemical", command=remove_last_chemical)
remove_chemical_button.grid(row=3, column=2, columnspan=3, pady=5)

# Preview Text
preview_text = tk.Text(preview_frame, width=60, height=40, state="disabled", wrap="word")
preview_text.pack(padx=5, pady=5)

# Populate Dropdowns
if hasattr(bacteria, "bacteria_list"):
    specimen_dropdown["values"] = list(bacteria.bacteria_list)
if hasattr(media, "media_list"):
    media_dropdown["values"] = [value["name"] for key, value in media.media_list.items()]
if hasattr(supplies, "general_supplies"):
    supply_dropdown["values"] = list(supplies.general_supplies.keys())
if hasattr(media, "media_list"):
    media_uninoc_dropdown["values"] = [value["name"] for key, value in media.media_list.items()]
if hasattr(chemicals, "chemicals"):
    chemical_dropdown["values"] = list(chemicals.chemicals.keys())

# --- Function to export summary to CSV ---
def export_summary():
    global current_experiment, experiments, biologicals_list, supplies_list, media_list, chemicals_list

    # Ensure current_experiment is not empty
    if current_experiment:
        # Ensure the experiment data is properly populated
        experiments[current_experiment] = {
            "biologicals": biologicals_list.copy(),
            "supplies": supplies_list.copy(),
            "media": media_list.copy(),
            "chemicals": chemicals_list.copy()
        }

    # Debugging: Print the data about to be exported
    print("Current experiment name:", current_experiment)
    print("Experiments stored:", experiments)

    # Debugging: Print lists to check if they are populated correctly
    print("Biologicals List:", biologicals_list)
    print("Supplies List:", supplies_list)
    print("Media List:", media_list)
    print("Chemicals List:", chemicals_list)

    # Ask where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Experiment Summary As"
    )

    if not file_path:
        return  # User cancelled the save operation

    # Write data to CSV
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["Experiment", "Type", "Item", "Amount", "Unit", "Cost"])

        # Write data for each experiment
        for experiment_name, data in experiments.items():
            for section_name, items in data.items():
                for item in items:
                    writer.writerow([
                        experiment_name,
                        section_name.capitalize(),
                        item.get("name", ""),
                        item.get("amount", ""),
                        item.get("unit", ""),
                        item.get("cost", "")
                    ])
    print("CSV Exported Successfully!")

def export_csv(file_path):
    global biologicals_list, supplies_list, media_list, chemicals_list, experiments

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Header
        writer.writerow(["Experiment Name", experiment_name.get()])
        writer.writerow(["Course", course_type_var.get()])
        course = courseinfo.courses.get(course_type_var.get())
        if course:
            writer.writerow(["Sections", course.sections])
            writer.writerow(["Groups", course.groups])
            writer.writerow(["Students", course.students])
        writer.writerow([])

        # Biologicals
        writer.writerow(["Biologicals"])
        writer.writerow(["Specimen", "Media", "Type", "Distribution", "Cost"])
        for b in added_biologicals:
            writer.writerow([b['specimen'], b['media'], b['type'], b['distribution'], b['cost']])
        writer.writerow([])

        # Supplies
        writer.writerow(["Supplies"])
        writer.writerow(["Name", "Distribution", "Cost"])
        for s in added_supplies:
            writer.writerow([s['name'], s['distribution'], s['cost']])
        writer.writerow([])

        # Media
        writer.writerow(["Uninoculated Media"])
        writer.writerow(["Media", "Type", "Distribution", "Cost"])
        for m in added_uninoculated_media:
            writer.writerow([m['media'], m['type'], m['distribution'], m['cost']])
        writer.writerow([])

        # Chemicals
        writer.writerow(["Chemicals"])
        writer.writerow(["Chemical", "Type", "Distribution", "Cost"])
        for c in added_chemicals:
            writer.writerow([c['chemical'], c['type'], c['distribution'], c['cost']])
        writer.writerow([])

# export summary buttons

export_button = ttk.Button(preview_frame, text="Export Summary", command=export_summary)
export_button.pack(pady=10)
   
root.mainloop()