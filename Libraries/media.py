#media.py

standard_volumes_ml = {
    "plate": 15, #mL per plate, Carrie says 15, but premade are 20... ##if plate only, need to add the cost of empty petri dish
    "slant": 5, #mL per slant tube
    "deep": 9, #mL per deep tube
    "broth": 9, #mL per broth tube
    "microcentrifuge_tube": 0.5, #500uL per microcentrifuge tube
    "premade": 0 #premaid plates do not use mL-based calculations
}

#media amounts
    #durum tube 9 ml
    #ec broth 9ml
    #luros tripos broth 9
    #nitrate broth 9
    #pbb tubex 9
    #other broth or agar are 5
    #plates 15
#empty petri plate 500 plates 97.64 ... ask her where she got this number, the packing slip says 83.64; either way added it to supplies.py

#media costs
media_list = {
    "nutrient_agar": {
        "name": "Nutrient Agar (NA)",
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep", "premade"],
        "premade_plate_cost": 17.82,  # cost per box of premade plates
        "plates_per_box": 10  # number of plates per box
    },

    "nutrient_broth": {
        "name": "Nutrient Broth (NB)",
        "cost_per_ml": 0.02,  # cost per mL
        "distribution": ["broth"]
    },

    "macconkey_agar": {
        "name": "MacConkey Agar (MAC)",
        "cost_per_ml": 0.017,  # cost per mL
        "distribution": ["plate"],
    },

    "blood_agar": {
        "name": "Blood Agar (BA)",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 78.63,  # cost per box of premade BA plates
        "plates_per_box": 100  # number of plates per box
    },

    "rabbit_coagulase_plasma": {
        "name": "Rabbit Coagulase Plasma (RCP)",
        "cost_per_ml": 3.21,  # cost per mL
        "distribution": ["microcentrifuge_tube"]
    },

    "tryptic_soy_agar": {
        "name": "Tryptic Soy Agar (TSA)",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 24.15,  # cost per box of premade TSA plates
        "plates_per_box": 10  # number of plates per box
    },

    "tryptic_soy_broth": { #tripic soy broth tsb $88.59 500g makes 4000 tubes
        "name": "Tryptic Soy Broth (TSB)",
        "cost_per_ml": 0.0025,  # cost per mL; 500g makes 4000 tubes, $88.59/4000 = $0.0221475/tube each tube has 9ml, so $0.0025/ml
        "distribution": ["broth"]
    },

    "mendo_plates": {
        "name": "mENDO Plates",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 44.98,  # cost per box of premade mENDO plates
        "plates_per_box": 10
    },

    "rodac_plates": {
        "name": "RODAC Plates",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 121.61,  # cost per box of premade RODAC plates
        "plates_per_box": 10
    },

    "columbia_cna_plates": {
        "name": "Columbia CNA Plates",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 45.88,  # cost per box of premade CNA plates
        "plates_per_box": 10
    },

    "mannitol_salt_agar": { #MSA (manatal salt agar) media alone $114.95 for 1 bottle, makes 300 plates
        "name": "Mannitol Salt Agar (MSA)",
        "cost_per_ml": 0.0255,  # cost per mL; 300x15ml = 4500ml, $114.95/4500ml = $0.0255/ml
        "distribution": ["slant", "plate"]
    },

    "bhi_broth": { #BHI broth $146.79 for 500g makes 2702 tubes
        "name": "Brain Heart Infusion Broth (BHI)",
        "cost_per_ml": 0.0326,  # cost per mL; 500g makes 2702 tubes, $146.79/2702 = $0.29358/tube each tube has 9ml, so $0.0326/ml
        "distribution": ["broth"]
    },

    "bile_esculin_agar": { #Bile esculin agar (BEA) $ 157.22 for 500g makes 1612 tubes
        "name": "Bile Esculin Agar (BEA)",
        "cost_per_ml": 0.0195, #1612x5ml = 8060ml, $157.22/8060ml = $0.0195/ml
        "distribution": ["slant", "plate"]
    },

    "tsia_slants": { #TSIA slants $148.94 for 500g makes 7692 tubes
        "name": "Triple Sugar Iron Agar (TSIA)",
        "cost_per_ml": 0.0039,  # $148.94/7692 = $0.01935/tube each tube has 5ml, so $0.00387/ml
        "distribution": ["slant"]
    },

"motility_media": { #motility media $201.75 for 500g makes 2777 tubes
        "name": "Motility Media",
        "cost_per_ml": 0.0036,  # $201.75/2777 = $0.0726/tube each tube has 9ml, so $0.0036/ml
        "distribution": ["broth"]
    },

"hek_plates": { #hek plates 500g 177.04 makes 434 plates
        "name": "Hektoen enteric (HEK, HE, HEA) Plates",
        "cost_per_ml": 0.354,  # $177.04/434 = $0.408/tube each tube has 15ml, so $0.354/ml
        "distribution": ["plate"]
    },

"xl_plate": { #xld plates premade 100 plates 161.63
        "name": "Xylose Lysine Deoxycholate (XLD) Plates",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 161.63,  # cost per box of premade XLD plates
        "plates_per_box": 100
    },

"ss_agar": { #salmonella shigella agar 500g 169.84 makes 555 plates
        "name": "Salmonella Shigella (SS) Agar",
        "cost_per_ml": 0.305,  # $169.84/555 = $0.306/tube each tube has 15ml, so $0.305/ml
        "distribution": ["plate"]
    },

"emb_plate": { #emb plate 500g bottle 176.65 makes 891 plates
        "name": "Eosin Methylene Blue (EMB) Plates",
        "cost_per_ml": 0.198,  # $176.65/891 = $0.198/tube each tube has 15ml, so $0.198/ml
        "distribution": ["plate"]
    },

"dnase_plate": { #dnase plates 500g bottle 756.96 makes 793 plates
        "name": "DNase Agar Plates",
        "cost_per_ml": 0.0,  # only available as premade plates
        "distribution": ["premade"],
        "premade_plate_cost": 756.96,  # cost per box of premade DNase plates
        "plates_per_box": 793
    },

"decarb_broth": { #decarboxylate broth 500g 170.63 makes 9505 tubes
        "name": "Decarboxylate Broth",
        "cost_per_ml": 0.0179,  # $170.63/9505 = $0.0179/tube each tube has 9ml, so $0.0179/ml
        "distribution": ["broth"]
    }
}


# Function to calculate cost per unit
#def calculate_media_cost(media_key, quantity, distribution_type):
#    if media_key not in media:
#        return f"Error: {media_key} not found in media library."
#    
#    media_info = media[media_key]
#    
#    if "premade" in media_info["distribution"] and distribution_type == "premade":
#        cost_per_plate = media_info["premade_plate_cost"] / media_info["plates_per_box"]
#        return cost_per_plate * quantity
#    
#    elif distribution_type in standard_volumes:
#        if media_info["cost_per_ml"] > 0:
#            total_volume = quantity * standard_volumes_ml[distribution_type]
#            return total_volume * media_info["cost_per_ml"]
#        else:
#            return f"Error: {media_info['name']} is only available as premade plates."
#    
#    return f"Error: Invalid distribution type '{distribution_type}' for {media_info['name']}."


# Example usage
#if __name__ == "__main__":
#    media_name = "macconkey_agar"
#    quantity = 34
#    distribution = "plate"
#    
#    total_cost = calculate_media_cost(media_name, quantity, distribution)
#    print(f"Total cost for {quantity} {distribution}(s) of {media[media_name]['name']}: ${total_cost:.2f}")

