import json
import os

# Course info
sections = 3
students = 30
groups = 15
lab_fee = 125

# Load the JSON file
json_file_path = os.path.join("C:\\Users\\Kandriad\\Documents\\GitHub\\MICROcost\\Courses", "351L_experiments.json")

with open(json_file_path, "r") as file:
    experiments_data = json.load(file)

# Iterate through experiments
for exp_id, exp_details in experiments_data["experiments"].items():
    print(f"{exp_details['experiment_name']}")

    # Initialize total costs for this experiment
    total_media_cost = 0
    total_supplies_cost = 0

    # Handle bacteria
    if "bacteria" in exp_details and exp_details["bacteria"]:
        # Variables to store total samples for preparation and actual use
        total_bacteria_for_prep = 0
        total_bacteria_for_experiment = 0

        # Handle preparation bacteria
        if "prep_bacteria" in exp_details["bacteria"]:
            for bact_name, bact_info in exp_details["bacteria"]["prep_bacteria"].items():
                total_samples = bact_info['number_of_samples']
                if isinstance(total_samples, str):
                    if "per_group" in total_samples:
                        total_samples = groups * int(total_samples.split('_')[0])
                    elif "per_section" in total_samples:
                        total_samples = sections * int(total_samples.split('_')[0])
                    elif "per_student" in total_samples:
                        total_samples = students * int(total_samples.split('_')[0])

                total_bacteria_for_prep += total_samples
                print(f"  Bacteria (prep): {bact_info['name']} - Total Samples: {total_samples}")

        # Handle experimental bacteria
        if "experimental_bacteria" in exp_details["bacteria"]:
            for bact_name, bact_info in exp_details["bacteria"]["experimental_bacteria"].items():
                total_samples = bact_info['number_of_samples']
                if isinstance(total_samples, str):
                    if "per_group" in total_samples:
                        total_samples = groups * int(total_samples.split('_')[0])
                    elif "per_section" in total_samples:
                        total_samples = sections * int(total_samples.split('_')[0])
                    elif "per_student" in total_samples:
                        total_samples = students * int(total_samples.split('_')[0])

                total_bacteria_for_experiment += total_samples
                print(f"  Bacteria (experiment): {bact_info['name']} - Total Samples: {total_samples}")

        print(f"  Total Bacteria Used in Preparation (separate): {total_bacteria_for_prep}")
        print(f"  Total Bacteria Used in Experiment (mixture): {total_bacteria_for_experiment}")
    else:
        print("  No bacteria used in this experiment.")

    # Handle media
    if "media" in exp_details and exp_details["media"]:
        for media_type, media_list in exp_details["media"].items():
            for media_name, media_info in media_list.items():
                # Calculate total samples for media
                total_samples = media_info.get("total_samples", 0)
                if isinstance(total_samples, str):
                    if "per_group" in total_samples:
                        total_samples = groups * int(total_samples.split('_')[0])
                    elif "per_section" in total_samples:
                        total_samples = sections * int(total_samples.split('_')[0])
                    elif "per_student" in total_samples:
                        total_samples = students * int(total_samples.split('_')[0])

                # Check if cost per unit is available
                media_cost_per_unit = media_info.get("cost_per_unit", 0)
                total_media_cost += media_cost_per_unit * total_samples
                print(f"  Media: {media_name} ({media_info.get('distribution')}) - Total Samples: {total_samples} - Cost: ${media_cost_per_unit * total_samples:.2f}")
    else:
        print("  No media used in this experiment.")

    # Handle supplies
    if "supplies" in exp_details and exp_details["supplies"]:
        for supply_name, supply_info in exp_details["supplies"].items():
            # Calculate the quantity needed for the experiment
            quantity_needed = supply_info.get("quantity_needed_for_experiment", "Unknown")
            if isinstance(quantity_needed, str):
                if "per_group" in quantity_needed:
                    quantity_needed = groups * int(quantity_needed.split('_')[0])
                elif "per_section" in quantity_needed:
                    quantity_needed = sections * int(quantity_needed.split('_')[0])
                elif "per_student" in quantity_needed:
                    quantity_needed = students * int(quantity_needed.split('_')[0])

            # Calculate cost per unit (cost_per_unit is now used directly)
            supply_cost_per_unit = supply_info["cost_per_unit"]
            unit_quantity = supply_info["cost_per_unit"] / supply_info["quantity"]
            total_supplies_cost += unit_quantity * quantity_needed
            print(f"  Supply: {supply_name} - Quantity Used: {quantity_needed} - Cost: ${total_supplies_cost:.2f}")
    else:
        print("  No supplies used in this experiment.")

    # Calculate total cost for the experiment
    total_cost = total_media_cost + total_supplies_cost
    print(f"Total Cost for {exp_details['experiment_name']}: ${total_cost:.2f}")
    print("\n")  # Add spacing for readability
