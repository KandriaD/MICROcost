#media.py

standard_volumes_ml = {
    "plate": 15, #mL per plate, Carrie says 15, but premade are 20... ##if plate only, need to add the cost of empty petri dish
    "slant": 5, #mL per slant tube
    "deep": 9, #mL per deep tube
    "broth": 5, #mL per broth tube
    "broth_full": 9,
    "durham_tube": 9,
    "microcentrifuge_tube": 0.5, #500uL per microcentrifuge tube
    "premade": 1, #premaid plates do not use mL-based calculations
    "topper_test_tube": 5,
    "topper_microcentrifuge_tube": 1
}

media_list = {
    "bglb": {
        "name": "BGLB (Brillant Green Lactose Bile w/ Durham tubes)",
        "supplier": "VWR",
        "catalog_number": "90003-916",
        "cost_per_ml": 0.01942 #242.73 for 500g
    },

    "bhi_agar": {
        "name": "Brain Heart Infusion Agar (BHI)",
        "supplier": "VWR",
        "catalog_number": "90000-066",
        "cost_per_ml": 0.02111 #285.28 for 500g
    },

    "bhi_broth": {
        "name": "Brain Heart Infusion Broth (BHI)",
        "supplier": "VWR",
        "catalog_number": "90000-060",
        "cost_per_ml": 00 #182.31 for 500g
    },

    "bile_esculin_agar": {
        "name": "Bile Esculin Agar (BEA)",
        "supplier": "VWR",
        "catalog_number": "89405-170",
        "cost_per_ml": 0.02088 #168.41 for 500g
    },

    "blood_agar": {
        "name": "Blood Agar (BA) [premade]",
        "supplier": "VWR",
        "catalog_number": "10324-332",
        "cost_per_ml": 54.16/100 #premade
    },

    "campy_cva":{
        "name": "Campy CVA [premade]",
        "supplier": "VWR",
        "catalog_number": "89405-034",
        "cost_per_ml": 15.92/10 #premade
    },

    "chocolate_agar": {
        "name": "Chocolate agar [premade]",
        "supplier": "VWR",
        "catalog_number": "89407-118", #"90006-202" for pack of 100
        "cost_per_ml": 7.27/10 #premade
    },

    "cin_agar": {
        "name": "CIN Agar [premade]",
        "supplier": "VWR",
        "catalog_number": "89407-218",
        "cost_per_ml": 16.88/10 #premade
    },

    "cna_plates": {
        "name": "Columbia CNA Plates [premade]",
        "supplier": "VWR",
        "catalog_number": "470180-738",
        "cost_per_ml": 23.86/10 #premade
    },

    "cornmeal agar": {
        "name": "Cornmeal agar",
        "supplier": "VWR",
        "catalog_number": "61000-028", #changed on 2/27/25 from 90000-098 17g/L
        "cost_per_ml": 0.00996  ## $292.94 for 500g
    },

    "decarb_broth": { #decarboxylate broth 500g 170.63 makes 9505 tubes
        "name": "Decarboxylase Broth",
        "supplier": "VWR",
        "catalog_number": "95021-768",
        "cost_per_ml": 0.00421 # $200.17 for 500g
    },

    "dnase_agar": { 
        "name": "DNase Agar",
        "supplier": "VWR",
        "catalog_number": "95021-114",
        "cost_per_ml": 0.07472 #dnase 500g bottle makes 793 plates
    },

    "ec_broth": { 
        "name": "EC broth w/ Durham tubes",
        "supplier": "VWR",
        "catalog_number": "90002-320",
        "cost_per_ml": 196.50/500*37/1000
    },

    "emb": {
        "name": "Eosin Methylene Blue (EMB)",
        "supplier": "VWR",
        "catalog_number": "90000-122",
        "cost_per_ml": 000 #157.43 for 500g
    },

    "glucose_salts_broth": { 
        "name": "Glucose Salts Broth",
        "cost_per_ml": 0.0,  #we make it, is a mixture of salts
    },

    "hek_plates": { 
        "name": "Hektoen enteric (HEK) Plates",
        "supplier": "VWR",
        "catalog_number": "95021-880",
        "cost_per_ml": 201.90/500*76.67/1000
    },

    "lauryl_triptose_broth": { 
        "name": "Lauryl Tryptose Broth w/ Durham tubes",
        "supplier": "VWR",
        "catalog_number": "90001-770",
        "cost_per_ml": 0.01063  #149.33 for 500g
    },

    "lb_agar": {
        "name": "Luria-Bertani agar",
        "supplier": "VWR",
        "catalog_number": "90003-346",
        "cost_per_ml": 0.01324 # $165.55 for 500g
    },

    "lb_broth": {
        "name": "Lennox Broth (LB)",
        "supplier": "VWR",
        "catalog_number": "76346-580",
        "cost_per_ml": 0.00287 # $71.64 for 500g
    },
    
    "loeffler_agar_slants": { 
        "name": "Loeffler Agar Slants [premade]",
        "supplier": "VWR",
        "catalog_number": "89426-236",
        "cost_per_ml": 130.40/20 #premade
    },

    "lowenstein_jensen_slants": { 
        "name": "Lowensteun-Jensen Slants [premade]",
        "supplier": "VWR",
        "catalog_number": "90001-154",
        "cost_per_ml": 48.35/10  #premade
    },

    "mac": {
        "name": "MacConkey Agar (MAC)",
        "supplier": "VWR",
        "catalog_number": "90000-168",
        "cost_per_ml": 151.63/500*50/1000 # $151.63 for 500g ##50g/L
    },
    
    "marine_agar": {
        "name": "Marine Agar (MA)",
        "supplier": "VWR",
        "catalog_number": "89225-372",
        "cost_per_ml": 0.0  # $622.30 for 3kg
    },

    "marine_broth": {
        "name": "Marine Agar (MB)",
        "supplier": "VWR",
        "catalog_number": "95021-754",
        "cost_per_ml": 214.84/500*40.25/1000  #214.84 for 500g ##40.25g/L
    },

    "mendo_plates": {
        "name": "mENDO Plates [premade]",
        "supplier": "VWR",
        "catalog_number": "89407-156",
        "cost_per_ml": 11.36/10 #premade
    },
    
    "middlebrook_7h11_slants": {
        "name": "Middlebrook 7H11 Slants",
        "supplier": "VWR",
        "catalog_number": "52428-852",
        "cost_per_ml": 106.31/20  # 106.31 per pack of 20 
    },

    "middlebrook_7h9_broth": {
        "name": "Middlebrook 7H9 Broth",
        "supplier": "VWR",
        "catalog_number": "75993-550",
        "cost_per_ml": 109.16/20  # 109.16 per pack of 20 
        },

    "mineral oil": {
        "name": "Mineral Oil", #used to top the test tube 1ml for microcentrfuge or 5ml in test tubes, only for anerobic
        "supplier": "VWR",
        "catalog_number": "97062-604",
        "cost_per_ml": 34.45/1000 #34.45 cost per bottle of 1L
    },

    "motility_media": {
        "name": "Motility Media",
        "supplier": "VWR",
        "catalog_number": "95021-572",
        "cost_per_ml": 236.68/500*20/1000 #236.68 for 500g ##20g/1L
    },

    "mr_vp_broths": { 
        "name": "MR-VP Broths",
        "supplier": "VWR",
        "catalog_number": "75803-772",
        "cost_per_ml": 0.004  #117.73 for 500g
    },

    "msa": { #MSA (manatal salt agar) media alone $114.95 for 1 bottle, makes 300 plates
        "name": "Mannitol Salt Agar (MSA)",
        "supplier": "VWR",
        "catalog_number": '90000-182',
        "cost_per_ml": 102.61/500*111/1000 #102.61 for 500g ##111g/L
    },

    "mtm_agar": {
        "name": "Modified Thayer-Martin Agar [premade]",
        "supplier": "VWR",
        "catalog_number": "10324-496",
        "cost_per_ml": 16.04/10 #premade
    },

    "muller_hinton": {
        "name": "Muller-Hinton Agar",
        "supplier": "VWR",
        "catalog_number": '95039-350',
        "cost_per_ml": 165.75/500*38/1000
    },

    "nutrient_agar_powder": {
        "name": "Nutrient Agar (NA)",
        "supplier": "VWR",
        "catalog_number": "470227-474",
        "cost_per_ml": 0.00492  # cost per mL ##213.85 for 1kg
    },

    "nutrient_agar_plate_premade": {
        "name": "Nutrient Agar (NA) Plate [premade]",
        "supplier": "VWR",
        "catalog_number": "101106-820", 
        "cost_per_ml": 28.17/10 
    },

    "nutrient_broth": { #nb broth 500g makes 10961ml
        "name": "Nutrient Broth (NB)",
        "supplier": "VWR",
        "catalog_number": "470227-476",
        "cost_per_ml": 0.00177  # 196.46 per 1kg
    },

    "nutrient_gelatin": { 
        "name": "Nutrient Gelatin",
        "supplier": "VWR",
        "catalog_number": "89405-802",
        "cost_per_ml": 167.92/500*128/1000
    },

    "of": { 
        "name": "O-F Media",
        "supplier": "VWR",
        "catalog_number": "90003-810",
        "cost_per_ml": 198.78/500*9.4/1000
    },
    
    "pbb": {
        "name": "Purple Broth Base (PBB)",
        "supplier": "VWR",
        "catalog_number": "90001-686", 
        "cost_per_ml": 251.33/500*15/1000
    },

    "pda": {
        "name": "Potato Dextrose Agar",
        "supplier": "VWR",
        "catalog_number": "90000-758", 
        "cost_per_ml": 193.69/500*39/1000
    },

    "pea": {
        "name": "Phenylethylalanine",
        "supplier": "VWR",
        "catalog_number": "89405-884", 
        "cost_per_ml": 0.0 #192.52 for 500g
    },

    "phenylalinine_agar": {
        "name": "Phenylalinine Agar",
        "supplier": "VWR",
        "catalog_number": "89405-884", 
        "cost_per_ml": 0.0089
    },   
    
    "potassium_tellurite_agar": {
        "name": "Potassium Tellurite Agar [premade]",
        "supplier": "Fischer Scientific",
        "catalog_number": "50-948-700",
        "cost_per_ml": 84.96/20 #premade
    },

    "r2a":{
        "name": "R2A", #stored in 401 fridge
        "supplier": "VWR",
        "catalog_number": "90000-994", 
        "cost_per_ml": 245.34/500*18.2/1000
    },

    "rcp": {
        "name": "Rabbit Coagulase Plasma (RCP)",
        "supplier": "VWR",
        "catalog_number": "90003-150", 
        "cost_per_ml": 621.38/10/15,  # cost/ packs/ ml made per pack
    },

    "rodac_plates": {
        "name": "RODAC Plates [premade]",
        "supplier": "VWR",
        "catalog_number": "101205-670",
        "cost_per_ml": 22.34/10 #premade
    },

    "ss_agar": { #salmonella shigella agar 500g 169.84 makes 555 plates
        "name": "Salmonella Shigella (SS) Agar",
        "supplier": "VWR",
        "catalog_number": "90000-240",
        "cost_per_ml": 0.305,  # $169.84/555 = $0.306/tube each tube has 15ml, so $0.305/ml ##now $210.93
    },

    "sda":{
        "name": "Sabourad Dextrose Agar [premade]",
        "supplier": "VWR",
        "catalog_number": "470177-376",
        "cost_per_ml": 25.64/10 #premade
    },

    "sim": {
        "name": "SIM",
        "supplier": "VWR",
        "catolog_number": "90000-232",
        "cost_per_ml": 240.07/500*30/1000
    },

    "simmons_citrate": {
        "name": "Simmon's Citrate",
        "supplier": "VWR",
        "catolog_number": "470317-448",
        "cost_per_ml": 0.00527
    },    

    "skim_milk_agar":{
        "name": "Skim Milk Agar",
        "supplier": "VWR",
        "catolog_number": "90002-594",
        "cost_per_ml": 67.38/500*100/1000 #67.38 for 500g ##100g/L
    },

    "sporulating_agar": {
        "name": "AK Agar (Sporulating Agar)",
        "supplier": "VWR",
        "catolog_number": "90000-014",
        "cost_per_ml": 0.02385
    },

    "starch_agar": {
        "name": "Starch Agar",
        "supplier": "VWR",
        "catolog_number": "90003-890",
        "cost_per_ml": 246.75/500*25/1000 
    },

    "tcbs": {
        "name": "Thiosulfate-Citrate-Bile Salts-sucrose (TCBS)",
        "supplier": "VWR",
        "catolog_number": "89406-112",
        "cost_per_ml": 0.03591  #tcbs plate media 500g 224.45
    },

    "thioglycollate_broth": {
        "name": "Thioglycollate Broth",
        "supplier": "VWR",
        "catolog_number": "90001-878",
        "cost_per_ml": 126.10/500*29.8/1000
    },   

    "tinsdale_base": { 
        "name": "Tinsdale Base",
        "supplier": "VWR",
        "catolog_number": "90003-990",
        "cost_per_ml": (539.03/500*22.5)/500 #tinsdale agar base 500g 539.03; 22.5 g for 500ml media
    },

    "tinsdale_enrichment": { 
        "name": "Tinsdale Enrichment",
        "supplier": "VWR",
        "catolog_number": "90002-668",
        "cost_per_ml": 0.2957 #tinsdale enrichment 6 bottles total 600ml 1360.11, use 15ml into 100ml of base
    },

    "tributyrin": {
        "name": "Tributyruin (add-in)",
        "supplier": "VWR",
        "catolog_number": "IC10311180",
        "cost_per_ml": 0.0
    },

    "tributyrin_agar_base":{
        "name": "Tributyruin Agar Base",
        "supplier": "VWR",
        "catolog_number": "61000-694",
        "cost_per_ml": 0.00852
    },

    "tsa": {
        "name": "Tryptic Soy Agar (TSA)",
        "supplier": "VWR",
        "catolog_number": "89405-202",
        "cost_per_ml": 0.00876
    },

    "tsa_plates_premade": {
        "name": "Tryptic Soy Agar (TSA) Plates [premade]",
        "supplier": "VWR",
        "catolog_number": "101205-688",
        "cost_per_ml": 13.18/10 #premade
    },

    "tsb": { 
        "name": "Tryptic Soy Broth (TSB)",
        "supplier": "VWR",
        "catalog_number": "470227-520",
        "cost_per_ml": 0.00456
    },

    "tsia": { 
        "name": "Triple Sugar Iron Agar (TSIA)",
        "supplier": "VWR",
        "catalog_number": "90001-896",
        "cost_per_ml": 132.96/500*65/1000
    },

    "urea_slants": { 
        "name": "Urea Slants [premade]",
        "supplier": "VWR",
        "catalog_number": "10065-304",
        "cost_per_ml": 82.34/20 #premade
    },

    "xld_plate": { #xld plates premade 100 plates 161.63
        "name": "Xylose Lysine Deoxycholate (XLD) Plates [premade]",
        "supplier": "VWR",
        "catalog_number": "90006-218",
        "cost_per_ml": 144.48/100
    },

    "ym_agar": { #stored in 401
        "name": "Yeast Mold Agar",
        "supplier": "VWR",
        "catolog_number": "90003-874", 
        "cost_per_ml": 243.22/500*41/1000
    }
}


#test tubes o-f (oxidation fermentation) test tubes, no glucose base 500g 160.06, 53191ml
## glucose needs to be added into it, have and have had for a long time so no cost at this time.
