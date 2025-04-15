import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

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

# --- Global storage variables ---
added_biologicals = []
added_supplies = []
added_uninoculated_media = []
added_chemicals = []

class ScrollableFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class CostCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Microbiology Lab Cost Calculator")

        # Store items
        self.biologicals = []
        self.supplies = []
        self.uninoculated_media = []
        self.chemicals = []

        # Course Info Frame
        self.course_frame = ttk.LabelFrame(root, text="Course Info")
        self.course_frame.pack(fill="x", padx=10, pady=5)

        self.create_course_info_inputs()

        # Scrollable Frame
        self.scrollable_frame = ScrollableFrame(root)
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Sections
        self.create_biologicals_section()
        self.create_supplies_section()
        self.create_uninoculated_media_section()
        self.create_chemicals_section()

        # Cost Preview and Export
        self.cost_label = ttk.Label(root, text="Total Cost: $0.00")
        self.cost_label.pack(pady=5)

        export_button = ttk.Button(root, text="Export Summary", command=self.export_summary)
        export_button.pack(pady=5)

    def create_course_info_inputs(self):
        labels = ["Course Number", "Number of Sections", "Number of Students", "Number of Groups", "Room Number"]
        self.course_entries = {}

        for idx, label in enumerate(labels):
            ttk.Label(self.course_frame, text=label).grid(row=0, column=idx)
            entry = ttk.Entry(self.course_frame, width=15)
            entry.grid(row=1, column=idx, padx=2)
            self.course_entries[label] = entry

    def create_section(self, parent, title):
        frame = ttk.LabelFrame(parent.scrollable_frame, text=title)
        frame.pack(fill="x", pady=5)
        return frame

    def create_biologicals_section(self):
        self.bio_frame = self.create_section(self.scrollable_frame, "Biologicals")
        self.add_bio_button = ttk.Button(self.bio_frame, text="Add Biological", command=self.add_biological)
        self.add_bio_button.pack(side="left", padx=5)
        self.remove_bio_button = ttk.Button(self.bio_frame, text="Remove Last", command=self.remove_last_biological)
        self.remove_bio_button.pack(side="left", padx=5)

    def add_biological(self):
        row = ttk.Frame(self.bio_frame)
        row.pack(fill="x", pady=2)

        specimen = ttk.Combobox(row, values=list(bacteria.bacteria_dict.keys()), width=20)
        specimen.pack(side="left", padx=5)

        media_choice = ttk.Combobox(row, values=list(media.media_dict.keys()), width=20)
        media_choice.pack(side="left", padx=5)

        distribution = ttk.Combobox(row, values=["plate", "slant", "deep", "premade", "microcentrifuge tube"], width=20)
        distribution.pack(side="left", padx=5)

        quantity = ttk.Entry(row, width=10)
        quantity.pack(side="left", padx=5)

        quantity_type = ttk.Combobox(row, values=["per student", "per group", "per section", "per table"], width=20)
        quantity_type.pack(side="left", padx=5)

        self.biologicals.append((row, specimen, media_choice, distribution, quantity, quantity_type))
        self.update_cost()

    def remove_last_biological(self):
        if self.biologicals:
            row, *_ = self.biologicals.pop()
            row.destroy()
            self.update_cost()

    def create_supplies_section(self):
        self.supply_frame = self.create_section(self.scrollable_frame, "Supplies")
        self.add_supply_button = ttk.Button(self.supply_frame, text="Add Supply", command=self.add_supply)
        self.add_supply_button.pack(side="left", padx=5)
        self.remove_supply_button = ttk.Button(self.supply_frame, text="Remove Last", command=self.remove_last_supply)
        self.remove_supply_button.pack(side="left", padx=5)

    def add_supply(self):
        row = ttk.Frame(self.supply_frame)
        row.pack(fill="x", pady=2)

        item = ttk.Combobox(row, values=list(supplies.supplies_dict.keys()), width=30)
        item.pack(side="left", padx=5)

        quantity = ttk.Entry(row, width=10)
        quantity.pack(side="left", padx=5)

        quantity_type = ttk.Combobox(row, values=["per student", "per group", "per section", "per table"], width=20)
        quantity_type.pack(side="left", padx=5)

        self.supplies.append((row, item, quantity, quantity_type))
        self.update_cost()

    def remove_last_supply(self):
        if self.supplies:
            row, *_ = self.supplies.pop()
            row.destroy()
            self.update_cost()

    def create_uninoculated_media_section(self):
        self.media_frame = self.create_section(self.scrollable_frame, "Uninoculated Media")
        self.add_media_button = ttk.Button(self.media_frame, text="Add Media", command=self.add_uninoculated_media)
        self.add_media_button.pack(side="left", padx=5)
        self.remove_media_button = ttk.Button(self.media_frame, text="Remove Last", command=self.remove_last_uninoculated_media)
        self.remove_media_button.pack(side="left", padx=5)

    def add_uninoculated_media(self):
        row = ttk.Frame(self.media_frame)
        row.pack(fill="x", pady=2)

        item = ttk.Combobox(row, values=list(media.media_dict.keys()), width=30)
        item.pack(side="left", padx=5)

        distribution = ttk.Combobox(row, values=["plate", "slant", "deep", "premade", "microcentrifuge tube"], width=20)
        distribution.pack(side="left", padx=5)

        quantity = ttk.Entry(row, width=10)
        quantity.pack(side="left", padx=5)

        quantity_type = ttk.Combobox(row, values=["per student", "per group", "per section", "per table"], width=20)
        quantity_type.pack(side="left", padx=5)

        self.uninoculated_media.append((row, item, distribution, quantity, quantity_type))
        self.update_cost()

    def remove_last_uninoculated_media(self):
        if self.uninoculated_media:
            row, *_ = self.uninoculated_media.pop()
            row.destroy()
            self.update_cost()

    def create_chemicals_section(self):
        self.chem_frame = self.create_section(self.scrollable_frame, "Chemicals")
        self.add_chem_button = ttk.Button(self.chem_frame, text="Add Chemical", command=self.add_chemical)
        self.add_chem_button.pack(side="left", padx=5)
        self.remove_chem_button = ttk.Button(self.chem_frame, text="Remove Last", command=self.remove_last_chemical)
        self.remove_chem_button.pack(side="left", padx=5)

    def add_chemical(self):
        row = ttk.Frame(self.chem_frame)
        row.pack(fill="x", pady=2)

        item = ttk.Combobox(row, values=list(chemicals.chemicals_dict.keys()), width=30)
        item.pack(side="left", padx=5)

        volume = ttk.Entry(row, width=10)
        volume.pack(side="left", padx=5)

        quantity_type = ttk.Combobox(row, values=["per student", "per group", "per section", "per table"], width=20)
        quantity_type.pack(side="left", padx=5)

        self.chemicals.append((row, item, volume, quantity_type))
        self.update_cost()

    def remove_last_chemical(self):
        if self.chemicals:
            row, *_ = self.chemicals.pop()
            row.destroy()
            self.update_cost()

    def update_cost(self):
        # Placeholder logic
        total_cost = 0.0
        self.cost_label.config(text=f"Total Cost: ${total_cost:.2f}")

    def export_summary(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        with open(file_path, "w") as f:
            f.write("Experiment Summary\n\n")
            f.write("Biologicals:\n")
            for row, specimen, media_choice, distribution, quantity, quantity_type in self.biologicals:
                f.write(f"  {specimen.get()}, {media_choice.get()}, {distribution.get()}, {quantity.get()}, {quantity_type.get()}\n")

            f.write("\nSupplies:\n")
            for row, item, quantity, quantity_type in self.supplies:
                f.write(f"  {item.get()}, {quantity.get()}, {quantity_type.get()}\n")

            f.write("\nUninoculated Media:\n")
            for row, item, distribution, quantity, quantity_type in self.uninoculated_media:
                f.write(f"  {item.get()}, {distribution.get()}, {quantity.get()}, {quantity_type.get()}\n")

            f.write("\nChemicals:\n")
            for row, item, volume, quantity_type in self.chemicals:
                f.write(f"  {item.get()}, {volume.get()}, {quantity_type.get()}\n")

        print(f"Summary exported to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CostCalculatorApp(root)
    root.mainloop()
