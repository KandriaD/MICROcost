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
    "bea": { #Bile esculin agar (BEA) $ 157.22 for 500g makes 1612 tubes
        "name": "Bile Esculin Agar (BEA)",
        "cost_per_ml": 0.0195, #1612x5ml = 8060ml, $157.22/8060ml = $0.0195/ml
        "distribution": ["slant", "plate"]
    },

    "bhi_broth": { #BHI broth $146.79 for 500g makes 2702 tubes
        "name": "Brain Heart Infusion Broth (BHI)",
        "cost_per_ml": 0.0326,  # cost per mL; 500g makes 2702 tubes, $146.79/2702 = $0.29358/tube each tube has 9ml, so $0.0326/ml
        "distribution": ["broth"]
    },

    "blood_agar": {
        "name": "Blood Agar (BA)",
        "supplier": "VWR",
        "catalog_number": "10324-332",
        "distribution": ["premade"],
        "premade_plate_cost": 78.63,  # cost per box of premade BA plates
        "plates_per_box": 100  # number of plates per box
    },

    "campy_cva":{
        "name": "Campy CVA",
        "supplier": "VWR",
        "catalog_number": "89405-034",
        "distribution": ["premade"],
        "premade_plate_cost": 0000,  # cost per box of premade plates
        "plates_per_box": 10  # number of plates per box
    },

    "chocolate_agar": {
        "name": "Chocolate agar",
        "supplier": "VWR",
        "catalog_number": "89407-118", #"90006-202" for pack of 100
        "distribution": ["premade"],
        "premade_plate_cost": 0000,  # cost per box of premade plates
        "plates_per_box": 10  # number of plates per box
    },

    "cin_agar": {
        "name": "CIN Agar",
        "supplier": "VWR",
        "catalog_number": "89407-218",
        "distribution": ["premade"],
        "premade_plate_cost": 0000,  # cost per box of premade plates
        "plates_per_box": 10  # number of plates per box
    },

    "cna_plates": {
        "name": "Columbia CNA Plates",
        "supplier": "VWR",
        "catalog_number": "470180-738",
        "distribution": ["premade"],
        "premade_plate_cost": 45.88,  # cost per box of premade CNA plates
        "plates_per_box": 10
    },

    "cornmeal agar": {
        "name": "Cornmeal agar",
        "supplier": "VWR",
        "catalog_number": "61000-028", #changed on 2/27/25 from 90000-098 17g/L
        "cost_per_ml": 0.0,  # need to check new bottle to figure out how much 500g bottle makes when we order it
        "distribution": ["plate"]
    },

    "decarb_broth": { #decarboxylate broth 500g 170.63 makes 9505 tubes
        "name": "Decarboxylate Broth",
        "cost_per_ml": 0.0179,  # $170.63/9505 = $0.0179/tube each tube has 9ml, so $0.0179/ml
        "distribution": ["broth"]
    },

    "dnase_plate": { 
        "name": "DNase Agar Plates",
        "supplier": "VWR",
        "catalog_number": "95021-114",
        "cost_per_ml": 0.0636,  #dnase plates 500g bottle 756.96 makes 793 plates
        "distribution": ["plate"],
    },

    "emb_plate": { #emb plate 500g bottle 176.65 makes 891 plates
        "name": "Eosin Methylene Blue (EMB) Plates",
        "supplier": "VWR",
        "catalog_number": "90000-122",
        "cost_per_ml": 0.198,  # $176.65/891 = $0.198/tube each tube has 15ml, so $0.198/ml
        "distribution": ["plate"]
    },

    "hek_plates": { #hek plates 500g 177.04 makes 434 plates
        "name": "Hektoen enteric (HEK) Plates",
        "supplier": "VWR",
        "catalog_number": "95021-880",
        "cost_per_ml": 0.354,  # $177.04/434 = $0.408/tube each tube has 15ml, so $0.354/ml
        "distribution": ["plate"]
    },

    "lb_agar": {
        "name": "Luria-Bertani agar",
        "supplier": "VWR",
        "catalog_number": "90003-346",
        "cost_per_ml": 0.0,
        "distribution": ["plate"]
    },
    
    "mac": {
        "name": "MacConkey Agar (MAC)",
        "supplier": "VWR",
        "catalog_number": "90000-168",
        "cost_per_ml": 0.017,  # cost per mL
        "distribution": ["plate"]
    },
    
    "marine_agar": {
        "name": "Marine Agar (MA)",
        "supplier": "VWR",
        "catalog_number": "89225-372",
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep"],
    },

    "mendo_plates": {
        "name": "mENDO Plates",
        "supplier": "VWR",
        "catalog_number": "89407-156",
        "distribution": ["premade"],
        "premade_plate_cost": 44.98,  # cost per box of premade mENDO plates
        "plates_per_box": 10
    },

    "motility_media": { #motility media $201.75 for 500g makes 2777 tubes
        "name": "Motility Media",
        "supplier": "VWR",
        "catalog_number": "95021-572",
        "cost_per_ml": 0.0036,  # $201.75/2777 = $0.0726/tube each tube has 9ml, so $0.0036/ml
        "distribution": ["deep"]
    },

    "msa": { #MSA (manatal salt agar) media alone $114.95 for 1 bottle, makes 300 plates
        "name": "Mannitol Salt Agar (MSA)",
        "supplier": "VWR",
        "catalog_number": '90000-182',
        "cost_per_ml": 0.0255,  # cost per mL; 300x15ml = 4500ml, $114.95/4500ml = $0.0255/ml
        "distribution": ["slant", "plate"]
    },

    "mtm_agar": {
        "name": "Modified Thayer-Martin Agar",
        "supplier": "VWR",
        "catalog_number": "10324-496",
        "distribution": ["premade"],
        "premade_plate_cost": 0000,  # cost per box of premade plates
        "plates_per_box": 10
    },

    "muller_hinton":{
        "name": "Muller-Hinton Agar",
        "supplier": "VWR",
        "catalog_number": '95039-350',
        "cost_per_ml": 0.0, #muller hinton agar 500g 132.35, 13157ml
        "distribution": ["slant", "plate"]   
    },

    "nutrient_agar": {
        "name": "Nutrient Agar (NA)",
        "supplier": "VWR",
        "catalog_number": "101106-820", # catalog number for premade plates ### catalog number for powder 470227-474
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep", "premade"],
        "premade_plate_cost": 17.82,  # cost per box of premade plates
        "plates_per_box": 10  # number of plates per box
    },

    "nutrient_broth": { #nb broth 500g 87.69, 10961ml
        "name": "Nutrient Broth (NB)",
        "cost_per_ml": 0.02,  # cost per mL
        "distribution": ["broth"]
    },

    "pda": {
        "name": "Potato Dextrose Agar",
        "supplier": "VWR",
        "catalog_number": "90000-758", 
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep"],
    },

    "pea": {
        "name": "Phenylethylalanine",
        "supplier": "VWR",
        "catalog_number": "89405-884", 
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep"],
    },

    "r2a":{
        "name": "R2A", #stored in 401 fridge
        "supplier": "VWR",
        "catalog_number": "90000-994", 
        "cost_per_ml": 0.0,  # cost per mL
        "distribution": ["plate", "slant", "deep"],
    },

    "rcp": {
        "name": "Rabbit Coagulase Plasma (RCP)",
        "cost_per_ml": 3.21,  # cost per mL
        "distribution": ["microcentrifuge_tube"]
    },

    "rodac_plates": {
        "name": "RODAC Plates",
        "supplier": "VWR",
        "catalog_number": "101205-670",
        "distribution": ["premade"],
        "premade_plate_cost": 121.61,  # cost per box of premade RODAC plates
        "plates_per_box": 10
    },

    "ss_agar": { #salmonella shigella agar 500g 169.84 makes 555 plates
        "name": "Salmonella Shigella (SS) Agar",
        "supplier": "VWR",
        "catalog_number": "90000-240",
        "cost_per_ml": 0.305,  # $169.84/555 = $0.306/tube each tube has 15ml, so $0.305/ml
        "distribution": ["plate", "slant"]
    },

    "sda":{
        "name": "Sabourad Dextrose Agar",
        "supplier": "VWR",
        "catalog_number": "470177-376",
        "distribution": ["premade"],
        "premade_plate_cost": 0000,  # cost per box of premade plates
        "plates_per_box": 10
    },

    "serum_tellurite_agar": {
        "name": "Sabourad Dextrose Agar",
        "supplier": "Fischer Scientific",
        "catalog_number": "50-948-700",
        "distribution": ["premade"],
        "premade_plate_cost": 84.96,  # cost per box of premade plates
        "plates_per_box": 20
    },

    "skim_milk_agar":{
        "name": "Skim Milk Agar",
        "supplier": "VWR",
        "catolog_number": "90002-594",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"]
    },

    "spirit_blue_base":{
        "name": "Spirit Blue Base",
        "supplier": "VWR",
        "catolog_number": "90004-552",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"]
    },
    
    "spirit_blue_lipase": {
        "name": "Spirit Blue Lipase",
        "supplier": "VWR",
        "catolog_number": "BD215335",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"]
    },

    "starch_agar": {
        "name": "Starch Agar",
        "supplier": "VWR",
        "catolog_number": "90003-890",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"]
    },

    "tcbs": {
        "name": "Thiosulfate-Citrate-Bile Salts-sucrose (TCBS)",
        "supplier": "VWR",
        "catolog_number": "89406-112",
        "cost_per_ml": 0.0241,  #tcbs plate media 500g 137.16, 5681ml
        "distribution": ["plate", "slant"]
    },

    "tinsdale_base": { #tinsdale agar base 500g 434.02; 22.5 g for 500ml media
        "name": "Tinsdale Base",
        "supplier": "VWR",
        "catolog_number": "90003-990",
        "cost_per_ml": 0.0391,  
        "distribution": ["plate", "slant"]
    },

    "tinsdale_enrichment": { #tinsdale enrichment 6 bottles total 600ml 1360.11, use 15ml into 100ml of base
        "name": "Tinsdale Enrichment",
        "supplier": "VWR",
        "catolog_number": "90003-668",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"],
    },

    "tributyrin": {
        "name": "Tributyruin (add-in)",
        "supplier": "VWR",
        "catolog_number": "IC10311180",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"],
    },

    "tributyrin_agar_base":{
        "name": "Tributyruin Agar Base",
        "supplier": "VWR",
        "catolog_number": "61000-694",
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant"],
    },

    "tsa": {
        "name": "Tryptic Soy Agar (TSA)",
        "supplier": "VWR",
        "catolog_number": "89405-202", #cat_num for powder ##catalog_number for premade plates 101205-688
        "cost_per_ml": 0.0,  
        "distribution": ["premade", "plate", "slant", "deep"],
        "premade_plate_cost": 24.15,  # cost per box of premade TSA plates
        "plates_per_box": 10  # number of plates per box
    },

    "tsb": { #tripic soy broth tsb $88.59 500g makes 4000 tubes 
        "name": "Tryptic Soy Broth (TSB)",
        "cost_per_ml": 0.0025,  # cost per mL; 500g makes 4000 tubes, $88.59/4000 = $0.0221475/tube each tube has 9ml, so $0.0025/ml
        "distribution": ["broth"]
    },

    "tsia_slants": { #TSIA slants $148.94 for 500g makes 7692 tubes
        "name": "Triple Sugar Iron Agar (TSIA)",
        "cost_per_ml": 0.0039,  # $148.94/7692 = $0.01935/tube each tube has 5ml, so $0.00387/ml
        "distribution": ["slant"]
    },

    "xld_plate": { #xld plates premade 100 plates 161.63
        "name": "Xylose Lysine Deoxycholate (XLD) Plates",
        "supplier": "VWR",
        "catalog_number": "90006-218",
        "distribution": ["premade"],
        "premade_plate_cost": 161.63,  # cost per box of premade XLD plates
        "plates_per_box": 100
    },

    "ym_plus_nacl": {
        "name": "YM + NaCl",
        "supplier": "VWR",
        "catolog_number": "90003-874", 
        "cost_per_ml": 0.0,  
        "distribution": ["plate", "slant", "deep"],
    }
}


#test tubes o-f (oxidation fermentation) test tubes, no glucose base 500g 160.06, 53191ml
## glucose needs to be added into it, have and have had for a long time so no cost at this time.




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

