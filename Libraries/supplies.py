#cost of other materials that are not bacteria or media

supplies_list = {
    "serological_pipette_10mL": {
        "name": "Serological Pipette 10mL",
        "cost_per_case": 74.05,
        "quantity": 400
    },

    "serological_pipette_5mL": {
        "name": "Serological Pipette 5mL",
        "cost_per_case": 67.31,
        "quantity": 400
    },

    "biohazard_pipet_keeper": {
        "name": "Biohazard Pipet Keeper",
        "cost_per_case": 242.55,
        "quantity": 50
    },

    "red_autoclave_bag": {
        "name": "Autoclave Bag",
        "cost_per_case": 70.09,
        "quantity": 200
    },

    "isopropanol_vinyl_label": {
        "name": "Isopropanol Vinyl Label",
        "cost_per_package": 41.10,
        "quantity": 25
    },

    "empty_petri_dish": {
        "name": "Empty Petri Dish",
        "cost_per_case": 83.64,
        "quantity": 500
    },

    "api_20e_kit": {
        "name": "API 20E Kit",
        "cost_per_kit": 542.92,
        "quantity": 25
    },

    "api_zym": {
        "name": "API ZYM",
        "cost_per_kit": 579.86,
        "quantity": 25
    },

    "zyme_a_x2_reagent": {
        "name": "ZYME A X2 Reagent",
        "cost_per_pack": 56.38,
        "quantity": 16
    },  # 16x8mL vials (check this)

    "zyme_b_x2_reagent": {
        "name": "ZYME B X2 Reagent",
        "cost_per_pack": 56.28,
        "quantity": 10
    },  # 10x5mL vials (check this)

    "clear_tubing": {
        "name": "Tubing",
        "cost_per_25ft": 282.21, "quantity": 25},
    "sterile_swabs": {
        "name": "Sterile Swabs",
        "cost_per_package": 13.95,
        "quantity": 100
    },

    "gaspak_ez_campy_sachet": {
        "name": "GasPak EZ Campy Sachet",
        "cost_per_package": 113.03,
        "quantity": 20
    },

    "gaspak_anaerobe_sachet": {
        "name": "GasPak Anaerobe Sachet",
        "cost_per_package": 103.76,
        "quantity": 20
    },

    "durham_tube": { # 0.7mL tubes
        "name": "Durham Tube",
        "cost_per_package": 281.04,
        "quantity": 72
    },

    "lab_tape": {
        "name": "Lab Tape",
        "cost_per_rolls": 64.13,
        "quantity": 24
    },

    "steam_sterilization_integrator": {
        "name": "Steam Sterilization Integrator",
        "cost_per_100": 35.10,
        "quantity": 100
    },

    "plating_beads": {
        "name": "Plating Beads",
        "cost_per_bottle": 45.57,
        "quantity": 230 # 230g, using 3-4 beads per plate
    },  

    "label_maker_tape": {
        "name": "Label Maker Tape",
        "cost_per_labels": 12.99,
        "quantity": 540
    },

    "label_maker": {
        "name": "Label Maker",
        "cost": 17.95
    }
}






# Example function to calculate per-unit cost
#def get_unit_cost(item_key):
#    item = supplies.get(item_key)
#    if item and "cost_per_case" in item:
#        return item["cost_per_case"] / item["quantity"]
#    elif item and "cost_per_package" in item:
#        return item["cost_per_package"] / item["quantity"]
#    elif item and "cost_per_kit" in item:
#        return item["cost_per_kit"] / item["quantity"]
#    elif item and "cost_per_bottle" in item:
#        return item["cost_per_bottle"] / item["quantity"]
#    elif item and "cost_per_labels" in item:
#        return item["cost_per_labels"] / item["quantity"]
#    elif item and "cost" in item:  # Single cost items
#        return item["cost"]
#    else:
#        return None

# Example usage
#if __name__ == "__main__":
#    item_name = "empty_petri_dish"
#    cost_per_item = get_unit_cost(item_name)
#    if cost_per_item:
#        print(f"Cost per {supplies[item_name]['name']}: ${cost_per_item:.2f}")
#    else:
#        print(f"{item_name} not found in supplies.")