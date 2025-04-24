#chemical costs for microbio labs
#many chemicals, such as stains, we have had for many years and are effectively free at current
chemical_list = {
    "bleach": {
        "name": "Bleach (Sodium Hypochlorite)",
        "supplier": "Longs Drugs",
        "catalog_number": "",
        "cost_per_unit": 3.43, #"bleach" 3.43 for 43 oz
        "quantity": 1271.66 #ml
    },

    "crystal_violet": {
        "name": "Crystal Violet",
        "supplier": "VWR",
        "catalog_number": "95060-952",
        "cost_per_unit": 19.26,
        "quantity": 237 #mL
    },
    
    "decolorizer": {
        "name": "Decolorizer (95% Ethanol)",
        "supplier": "VWR",
        "catalog_number": "95060-952",
        "cost_per_unit": 0, #95% ethonol from chem stock room
        "quantity": 500 #mL
    },

    "dextrose":{
        "name": "Dextrose (D-Glucose)",
        "supplier": "VWR",
        "catalog_number": "BDH9230-500G",
        "cost_per_unit": 30.97, #cost per bottle of 500g
        "quantity": 500 #500g
    },

    "ferric_chloride": {
        "name": "Ferric Chloride [iron (III) chloride hexahydrate]",
        "supplier": "VWR",
        "catalog_number": "00-00", #look at Cas# on bottle and find cheap on on VWR
        "cost_per_unit": 0.00853,#cost per ml for 10%solution
        "quantity": 1  #42.64 for 500g then make a 10% solution in water
    },

    "fetal_bovine_serum": {
        "name": "Fetal Bovine Serum",
        "supplier": "VWR",
        "catalog_number": "76644-856",
        "cost_per_unit": 68.60,
        "quantity": 50 #50 mL
    },

    "glucose_salts": {
        "name": "Glucose Salts",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 00, #cost for 5ml 0.0014
        "quantity": 00
    },

    "hydrogen_peroxide": {
        "name": "3% Hydrogen Peroxide",
        "supplier": "Fisher Sci",
        "catalog_number": "0000", #need to get the catalog_number 
        "cost_per_unit": 36.03, #36.03/500ml for 30%
        "quantity": 5000 # 5000 mL when diluted to 3%
    },

    "india_ink":{
        "name": "India Ink Droppers",
        "supplier": "VWR",
        "catalog_number": "90003-681",
        "cost_per_unit": 97.50,
        "quantity": 50
    },

    "iodine": {
        "name": "Gram's Iodine",
        "supplier": "VWR",
        "catalog_number": "470301-184",
        "cost_per_unit": 69.45, 
        "quantity": 1000 #1000mL
    },

    "isopropanol_70%": { ####1.49, cost per bottle from LongsDrugs when on sale
        "name": "Isopropanol 70%",
        "supplier": "Longs Drugs",
        "catalog_number": "0000", #need to get the catalog_number
        "cost_per_unit": 2.59, #cost per bottle from LongsDrugs when not on sale
        "quantity": 500 # 500 mL
    },

    "kovacs_reagent":{
        "name": "Kovac's Reagent",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 310.39,
        "quantity": 50  #50 dropper ampules
    },

    "lactophenol_cotton_blue":{ #amplule
        "name": "Lactophenol Cotton Blue",
        "supplier": "VWR",
        "catalog_number": "90003-668",
        "cost_per_unit": 103.86, #cost per bottle of 100mL
        "quantity": 50 #ampules
    },

    "l_ornithine_hydrochloride": {
        "name": "L-Ornithine Hydrochloride",
        "supplier": "Fisher Scientific",
        "catalog_number": "BP389-100",
        "cost_per_unit": 86.88, #cost per bottle of 100g
        "quantity": 100 
    },

    "lysol": {
        "name": "Lysol (Disinfectant Spray)",
        "supplier": "Longs Drugs",
        "catalog_number": "",
        "cost_per_unit": 3.98, # 3.98 for 28 oz
        "quantity": 828.059 #ml
    },

    "maltose_monohydrate": {
        "name": "Maltose Monohydrate",
        "supplier": "VWR",
        "catalog_number": "97062-604",
        "cost_per_unit": 46.62, #cost per bottle of 100g
        "quantity": 100 
    },

    "methylene_blue":{
        "name": "Methylene Blue",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "ninhydrin": {
        "name": "Ninhydrin", 
        "supplier": "VWR",
        "catalog_number": "470301-874",
        "cost_per_unit":  16.50,
        "quantity": 500 #500 mL
    },

    "nitrate_reagent_a": {
        "name": "Nitrate reagent A",
        "supplier": "Millipore Sigma",
        "catalog_number": "38497",
        "cost_per_unit": 0,
        "quantity": 100
    }, 

    "nacl": {
        "name": "Sodium Chloride (NaCl)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0.03,
        "quantity": 500 #500ml
    },

    "nitrate_reagent_b": {
        "name": "Nitrate reagent B",
        "supplier": "Millipore Sigma",
        "catalog_number": "39441",
        "cost_per_unit": 0,
        "quantity": 100
    },

    "oxidrops": {
        "name": "Oxidrops Liquid (Oxidase Reagent)", #very short shelf life
        "supplier": "VWR",
        "catalog_number": "89428-918",
        "cost_per_unit": 30.19,
        "quantity": 30
    },

    "safranin":{
        "name": "Safranin",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

   "sodium_deoxycholate": {
        "name": "Sodium Deoxycholate", 
        "supplier": "VWR",
        "catalog_number": "97062-028",
        "cost_per_unit": 152.14,
        "quantity": 50
    },

    "tda_reagent": {
        "name": "TDA Reagent", 
        "supplier": "VWR",
        "catalog_number": "95060-952",
        "cost_per_unit": 60.04,
        "quantity": 10 #2x5mL
    },

    "tweeen_80": {
        "name": "Tween 80 (water soluble)", 
        "supplier": "VWR",
        "catalog_number": "76347-646",
        "cost_per_unit": 38.11,
        "quantity": 500  
    },

    "ziehl_neelsen_carbolfuchsin": {
        "name": "Ziehl-Neelsen Carbolfuchsin", 
        "supplier": "VWR",
        "catalog_number": "76591-146",
        "cost_per_unit": 27.95,
        "quantity": 236 #8oz = 236.588 ml
    },

    "zinc_powder":{
        "name": "Zinc Powder",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 14.51, #14.51 for 25g, only use 0.01g per use
        "quantity": 2500 #number of uses per container
    }
}

