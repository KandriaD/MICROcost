#chemical costs for microbio labs
#many chemicals, such as stains, we have had for many years and are effectively free at current
chemical_list = {
    "20mm_phosphate_buffer": {
        "name": "20mM Phosphate Buffer (pH 7.0)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0.0, #need to get this information
        "quantity": 1 
    },

    "ferric_chloride": {
        "name": "10% Ferric Chloride Solution",
        "supplier": "VWR",
        "catalog_number": "00-00", #look at Cas# on bottle and find cheap on on VWR
        "cost_per_unit": 0.00853, #cost per ml for 10%solution
        "quantity": 1  #42.64 for 500g then make a 10% solution in water
    },

    "acetic_acid": {
        "name": "Acetic Acid",
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 36.82, 
        "quantity": 500 #500ml
    },

    "acid_alcohol": {
        "name": "Acid Alcohol (3% HCl in Ethanol)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 68, #this is cost of ethonol only #3% HCl in ethanol from chem stock room
        "quantity": 1000 #mL
    },

    "biorad_dc_protein_assay_kit_reagentA": {
        "name": "Biorad DC Protein Assay Kit Reagent A (Alkaline Copper Tartrate)",
        "supplier": "Bio Rad",
        "catalog_number": "5000111",
        "cost_per_unit": 30.83, #$278 for kit includes 250ml alkaline copper tartrate, 2L dilute Foiin reagent, 5ml surfactant solution, bovine y-globulin standard; 450 assays
        "quantity": 250
    },

    "biorad_dc_protein_assay_kit_reagentB": {
        "name": "Biorad DC Protein Assay Kit Reagent B (Folin Reagent)",
        "supplier": "Bio Rad",
        "catalog_number": "5000111",
        "cost_per_unit": 246.60, #$278 for kit includes 250ml alkaline copper tartrate, 2L dilute Foiin reagent, 5ml surfactant solution, bovine y-globulin standard; 450 assays
        "quantity": 2000 #2L dilute Folin reagent
    },

    "bleach": {
        "name": "Bleach (Sodium Hypochlorite)",
        "synonym": ["Sodium Hypochlorite", "Bleach"],
        "supplier": "Longs Drugs",
        "catalog_number": "",
        "cost_per_unit": 3.43, #"bleach" 3.43 for 43 oz
        "quantity": 1271.66 #ml
    },

    "blocking_solution": {
        "name": "Blocking Solution (1% BSA and 0.05% Tween 20 in PBS)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 127.08,
        "quantity": 1000 #1000ml
    },

    "borate_buffered_saline": {
        "name": "Borate Buffered Saline (BBS)",
        "synonym": ["Borate Buffered Saline", "BBS"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0.003,
        "quantity": 1 #0.17 M borate + 0.12 M NaCl, comes out to $0.00317 per ml
    },

    "borate_solution": {
        "name": "Borate Solution",
        "supplier": "VWR",
        "catalog_number": "BT222805",
        "cost_per_unit": 23.59,
        "quantity": 500 #23.59 for 500g; density 1.73g/ml, mm 381.37 g/mol
    },

    "congo_red": {
        "name": "Congo Red",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need to get this information
        "quantity": 1
    },

    "coomassie_blue": {
        "name": "Coomassie Blue R-250",
        "supplier": "Bio-Rad",
        "catalog_number": "1610435",
        "cost_per_unit": 197*(1/3), #kit contatins 1L stain and 2L destain
        "quantity": 1000 #1L
    },

    "coomassie_gel_destain": {
        "name": "Coomassie Gel Destain",
        "supplier": "Bio-Rad",
        "catalog_number": "1610435",
        "cost_per_unit": 197*(2/3), #kit contatins 1L stain and 2L destain
        "quantity": 2000 #2L
    },

    "coomassie_gel_stain": {
        "name": "Coomassie Gel Stain",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 8.83,
        "quantity": 1000 #1L
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
        "cost_per_unit": 68, #95% ethonol from chem stock room
        "quantity": 1000 #mL
    },

    "ddh2o": {
        "name": "ddH2O",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, 
        "quantity": 1 
    },

    "dextrose":{
        "name": "Dextrose (D-Glucose)",
        "supplier": "VWR",
        "catalog_number": "BDH9230-500G",
        "cost_per_unit": 30.97, #cost per bottle of 500g
        "quantity": 500 #500g
    },

    "dimethylaminocinnamaldehyde": {
        "name": "0.01% - 𝛒-Dimethylaminocinnamaldehyde (DMACA)",
        "synonym": ["DMACA", "Dimethylaminocinnamaldehyde","0.01% - 𝛒-dimethylaminocinnamaldehyde"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need to get this information
        "quantity": 1
    },

    "dpbs": {
        "name": "Dulbecco's Phosphate Buffered Saline (DPBS)",
        "supplier": "VWR",
        "catalog_number": "45000-426",
        "cost_per_unit": 164.82/6/500, #500ml per bottle, pack of 6
        "quantity": 1 #1ml
    },

    "70%_ethanol": {
        "name": "Ethanol (70%)",
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 13.2*70/95, #95% ethonol from chem stock room
        "quantity": 3785.41 #1 gallon = 3785.41 mL
    },

    "95%_ethanol": {
        "name": "Ethanol (95%)",
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 13.20, #95% ethonol from chem stock room
        "quantity": 3785.41 #1 gallon = 3785.41 mL
    },

    "ethanol_acetic_acid": {
        "name": "Ethanol : Acetic Acid (2:1)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 2.69, 
        "quantity": 100 #100mL
    },

    "freezing_medium": {
        "name": "Freezing Medium (10% gylcerol in 100% Fetal Bovine Serum)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 176.28, 
        "quantity": 100 #100mL
    },

    "glycerol": {
        "name": "Glycerol",
        "supplier": "Millipore Sigma",
        "catalog_number": "G5516",
        "cost_per_unit": 104, #cost per bottle of 500ml
        "quantity": 500 #500ml
    },

    "glycine": {
        "name": "Glycine Buffer (0.1M)",
        "supplier": "VWR",
        "catalog_number": "JT4059-0",
        "cost_per_unit": 81.97, #81.97 for 250g of pure, need 0.1M solution
        "quantity": 33300 #33300 mL of 0.1M solution
    },

    "hay_infusion": {
        "name": "Hay Infusion",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, 
        "quantity": 1 
    },

    "hcl": {
        "name": "Hydrochloric Acid (HCl)",
        "synonym": ["HCl", "Hydrochloric Acid"],
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 18.19,
        "quantity": 500 #500ml
    },

    "hydrogen_peroxide": {
        "name": "Hydrogen Peroxide (30%)",
        "synonym": ["H2O2", "Hydrogen Peroxide"],
        "supplier": "Fisher Sci",
        "catalog_number": "0000", #need to get the catalog_number 
        "cost_per_unit": 36.03, #36.03/500ml for 30%
        "quantity": 500 
    },

    "hydrogen_peroxide_3%_in_pbs": {
        "name": "Hydrogen Peroxide (3%) in PBS",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0.8131, 
        "quantity": 100 #100ml
    },

    "iodine": {
        "name": "Gram's Iodine",
        "synonym": ["Iodine", "Gram Iodine"],
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

    "kinyounin_carbolfuchsin": {
        "name": "Kinyoun's Carbolfuchsin",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #have not purchased this in a long time
        "quantity": 1
    },

    "koh": {
        "name": "Potassium Hydroxide (KOH)",
        "synonym": ["KOH", "Potassium Hydroxide"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "kmno4": {
        "name": "Potassium Permanganate (KMnO4)",
        "synonym": ["KMnO4", "Potassium Permanganate", "Potassium Permanganate Solution"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "kovacs_reagent":{
        "name": "Kovac's Reagent",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 310.39,
        "quantity": 50  #50 dropper ampules
    },

    "pondwater": {
        "name": "Pond Water",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, 
        "quantity": 1
    },

    "lactophenol_cotton_blue":{ #amplule
        "name": "Lactophenol Cotton Blue",
        "supplier": "VWR",
        "catalog_number": "90003-668",
        "cost_per_unit": 103.86, #cost per bottle of 100mL
        "quantity": 50 #ampules
    },

    "laemli_ssample_buffer": {
        "name": "Laemmli Sample Buffer (2x)",
        "supplier": "Bio-Rad",
        "catalog_number": "1610737",
        "cost_per_unit": 16,
        "quantity": 30 #30mL
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
        "synonym": ["Lysol", "Disinfectant Spray"],
        "supplier": "Longs Drugs",
        "catalog_number": "",
        "cost_per_unit": 3.98, # 3.98 for 28 oz
        "quantity": 828.059 #ml
    },

    "malachite_green": {
        "name": "Malachite Green",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1 #mL
    },

    "maltose_monohydrate": {
        "name": "Maltose Monohydrate",
        "supplier": "VWR",
        "catalog_number": "97062-604",
        "cost_per_unit": 46.62, #cost per bottle of 100g
        "quantity": 100 
    },

    "methanol": {
        "name": "Methanol",
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 34.27, 
        "quantity": 4000 #4L
    },

    "methylene_blue":{
        "name": "Methylene Blue",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "methyl_red": {
        "name": "Methyl Red",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "mgcl2": {
        "name": "MgCl2 0.1M",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need to get this information
        "quantity": 1
    },

    "nacl": {
        "name": "Sodium Chloride (NaCl)",
        "synonym": ["NaCl", "Sodium Chloride"],
        "supplier": "VWR",
        "catalog_number": "470302-522",
        "cost_per_unit": 7.46,
        "quantity": 500 #500g
    },

    "n-butanol": {
        "name": "n-Butanol",
        "supplier": "UH Chem Stock Room",
        "catalog_number": "",
        "cost_per_unit": 25.46,
        "quantity": 1000 #1000mL
    },

    "ninhydrin": {
        "name": "Ninhydrin", 
        "supplier": "VWR",
        "catalog_number": "470301-874",
        "cost_per_unit":  16.50,
        "quantity": 500 #500 mL
    },

    "nigrosin": {
        "name": "Nigrosin",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, 
        "quantity": 1
    },

    "paraformaldehyde_4%": {
        "name": "Paraformaldehyde (4%)",
        "supplier": "VWR",
        "catalog_number": "101176-014",
        "cost_per_unit": 103.01, #cost for 4%
        "quantity": 1000
    },

    "paraformaldehyde_1%": {
        "name": "Paraformaldehyde (1%) in PBS",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 2.65,
        "quantity": 100 #100ml
    },

    "pbs": {
        "name": "Phosphate Buffered Saline (PBS)",
        "synonym": ["PBS", "Phosphate Buffered Saline"],
        "supplier": "VWR",
        "catalog_number": "76371-734",
        "cost_per_unit": 102.81/100/1000, #in powder packs, 1 pack makes 1L, 100 packs per box $102.81
        "quantity": 1 #1ml
    },

    "petroleum_jelly": {
        "name": "Petroleum Jelly",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need get this information
        "quantity": 1 #need to get this information
    },
        
    "poly_l_lysine": {
        "name": "Poly-L-Lysine",
        "supplier": "Millipore Sigma",
        "catalog_number": "P8920",
        "cost_per_unit": 157, # $157.00 for 100ml
        "quantity": 100 #100ml
    },

    "saline": {
        "name": "Saline (0.85% NaCl)",
        "synonym": ["Saline", "0.85% NaCl"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0.03,
        "quantity": 500 #500ml
    },

    "safranin":{
        "name": "Safranin",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "saturated_ammonium_sulfate": {
        "name": "Saturated Ammonium Sulfate (SAS)",
        "synonym": ["SAS", "Saturated Ammonium Sulfate"],
        "supplier": "VWR",
        "catalog_number": "470300-256",
        "cost_per_unit": 0.017, #15.38 for 500g, for 4.1M, $0.01667/ml solution
        "quantity": 1 #ml of solution
    },

    "sds": {
        "name": "Sodium Dodecyl Sulfate (SDS)",
        "synonym": ["SDS", "Sodium Dodecyl Sulfate"],
        "supplier": "VWR",
        "catalog_number": "97064-496",
        "cost_per_unit": 92.95, #cost per bottle of 100g
        "quantity": 100 #100g 
    },

    "seawater": {
        "name": "Seawater",
        "synonym": ["Seawater", "SW"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
    },

    "sigmafast_opd_hrp_substrate": {
        "name": "SigmaFast OPD HRP Substrate",
        "supplier": "Millipore Sigma",
        "catalog_number": "P9187",
        "cost_per_unit": 0.01, #cost per ml
        "quantity": 1000 #50 tablets, half tablet per 10ml, so 1000ml total is made
    },

    "sheep_red_blood_cells": {
        "name": "Sheep Red Blood Cells (SRBC)",
        "synonym": ["SRBC", "Sheep Red Blood Cells"],
        "supplier": "Rockland",
        "catalog_number": "R406-0050",
        "cost_per_unit": 431, #cost for 50ml
        "quantity": 50 
    },

    "sheep_red_blood_cells_2%": {
        "name": "2% SRBC in Saline",
        "supplier": "Rockland",
        "catalog_number": "R406-0050", #we dilute
        "cost_per_unit": 17.25, 
        "quantity": 100 #100ml
    },

    "sheep_red_blood_cells_4%": {
        "name": "4% SRBC in Saline",
        "supplier": "Rockland",
        "catalog_number": "R406-0050", #we dilute
        "cost_per_unit": 34.49, 
        "quantity": 100 #100ml 
    },

    "sodium_deoxycholate": {
        "name": "Sodium Deoxycholate", 
        "supplier": "VWR",
        "catalog_number": "97062-028",
        "cost_per_unit": 152.14,
        "quantity": 50
    },

    "sucrose": {
        "name": "Sucrose",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need to get this information
        "quantity": 1
    },

    "1x_tbs": {
        "name": "1x TBS (Tris Buffered Saline)",
        "synonym": ["1x TBS", "Tris Buffered Saline"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 3.56, #100ml tris base in 900ml water
        "quantity": 1000 #1000ml
    },

    "tda_reagent": {
        "name": "TDA Reagent", 
        "supplier": "VWR",
        "catalog_number": "95060-952",
        "cost_per_unit": 60.04,
        "quantity": 10 #2x5mL
    },

    "tg_salts": {
        "name": "TG Salts",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #need to get this information ###Per 1 L: 11.02g (CaCl2*2H2O; FW 147.02); 1.22g (MgCl2*6H2O; W 203.3); 150g glycerol
        "quantity": 1
    },

    "towbin_transfer_buffer": {
        "name": "Towbin Transfer Buffer",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 5.645, 
        "quantity": 1000 #cost per 1000ml
    },

    "tris_base": {
        "name": "Tris Base (1M)",
        "supplier": "VWR",
        "catalog_number": "95029-578",
        "cost_per_unit": 146.93, #cost per bottle of 500g
        "quantity": 4127 #4127mL of 1M solution
    },

    "tris_hcl": {
        "name": "Tris-HCl (1M)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 10, 
        "quantity": 3300 #33000mL of 1M solution for $10
    },

    "trypan_blue": {
        "name": "Trypan Blue Stain (0.1%)",
        "supplier": "VWR",
        "catalog_number": "97063-702",
        "cost_per_unit": 43.04, #cost per bottle of 100mL
        "quantity": 100*4 #need diluted to 0.1%
    },

    "trypan_blue_in_pbs": {
        "name": "Trypan Blue Stain (0.1%) in PBS", #changed to pbs instead of dpbs, didnt adjust numbers just name
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 148.81, 
        "quantity": 1000 #1000mL of 0.1% trypan blue in PBS 
    },

    "trypsin": {
        "name": "Trypsin (0.05% / mM EDTA)",
        "supplier": "VWR",
        "catalog_number": "45001-082",
        "cost_per_unit": 72.11, #cost per 6 bottle of 100ml
        "quantity": 600 #6 bottles of 100ml
    },

    "tween_20": {
        "name": "Tween 20 (0.05%)", 
        "supplier": "VWR",
        "catalog_number": "97062-332",
        "cost_per_unit": 0.049, #98.03 for 1000ml pure
        "quantity": 1000 
    },

    "tweeen_80": {
        "name": "Tween 80", 
        "supplier": "VWR",
        "catalog_number": "76347-646",
        "cost_per_unit": 38.11,
        "quantity": 500  
    },

    "vpa": {
        "name": "VP A", #for API 20E kit
        "supplier": "VWR",
        "catalog_number": "95060-978",
        "cost_per_unit": 60.04,  
        "quantity": 10 #2x5ml
    },

    "vpb": {
        "name": "VP B", #for API 20E kit
        "supplier": "VWR",
        "catalog_number": "95060-976",
        "cost_per_unit": 60.04,  
        "quantity": 10 #2x5ml
    },

    "washing_solution": {
        "name": "Washing Solution (0.05% Tween 20 in PBS)",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 54.94, 
        "quantity": 1000 #1000ml
    },

    "water": {
        "name": "Water (distilled)",
        "synonym": ["Distilled Water", "Water", "sterile water"],
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0,
        "quantity": 1
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
    },

#serums, antiserums, and such
    "1ab_antibody": {
        "name": "1° Ab antibody",
        "supplier": "",
        "catalog_number": "",
        "cost_per_unit": 0, #still need to get this information
        "quantity": 1 
    },

    "2ab_antibody": {
        "name": "2° Ab antibody",
        "supplier": "Millipore Sigma",
        "catalog_number": "A542C",
        "cost_per_unit": 252,  
        "quantity": 1 #1ml is 1000 ul
    },

    "2ab_antibody_solution": {
        "name": "2° Ab antibody solution (rabbit anit-goat IgG-HRP in 0.5% BSA/TBS)",
        "supplier": "",
        "catalog_number": "", #we mix
        "cost_per_unit": 13.02, #based on 1:2000 dilution of antibody with all other components
        "quantity": 100 #ml
    },

    "antibiodies_anti-bovine": {
        "name": "Antibodies (Anti-Bovine IgG)",
        "supplier": "Millipore Sigma",
        "catalog_number": "B1520",
        "cost_per_unit": 557, #cost per vial
        "quantity": 2 #2ml vial = 2000ul
    },

    "antibiodies_anti-human": {
        "name": "Antibodies (Anti-Human IgG)",
        "supplier": "Millipore Sigma",
        "catalog_number": "AP114P",
        "cost_per_unit": 267, #cost per vial
        "quantity": 2 #2ml vial = 2000ul
    },

    "antibiodies_anti-goat": {
        "name": "Antibodies (Anti-Goat IgG)",
        "supplier": "Millipore Sigma",
        "catalog_number": "A5420",
        "cost_per_unit": 252.00, #cost per vial
        "quantity": 1 #1ml vial = 1000ul
    },

    "antibiodies_anti-mouse": {
        "name": "Antibodies (Anti-Mouse IgG)",
        "supplier": "Millipore Sigma",
        "catalog_number": "F1010",
        "cost_per_unit": 392, #cost per vial
        "quantity": 1 #1ml vial = 1000ul
    },

    "antibiodies_anti-rabbit": {
        "name": "Antibodies (Anti-Rabbit IgG)",
        "supplier": "Millipore Sigma",
        "catalog_number": "R5131",
        "cost_per_unit": 156, #cost per vial
        "quantity": 2 #2ml vial = 2000ul
    },

    "bsa": {
        "name": "Bovine Serum Albumin (BSA) (1%)",
        "synonym": ["BSA", "Bovine Serum Albumin", "Bovine Serum Albumin (BSA)"],
        "supplier": "Millipore Sigma",
        "catalog_number": "126609",
        "cost_per_unit": 1260, #cost per bottle of 100g
        "quantity": 10000 #need at 1%, so 1g in 100ml, 10000 ml produced per bottle
    },

    "fetal_bovine_serum_100%": {
        "name": "Fetal Bovine Serum (100%)",
        "synonym": "FBS",
        "supplier": "VWR",
        "catalog_number": "89510-194",
        "cost_per_unit": 96.78, #cost per bottle of 50ml
        "quantity": 50 #50ml
    },
    
    # "fetal_bovine_serum": {
    #     "name": "Fetal Bovine Serum",
    #     "supplier": "VWR",
    #     "catalog_number": "76644-856",
    #     "cost_per_unit": 68.60,
    #     "quantity": 50 #50 mL
    # },

    "goat_antihuman_igg": {
        "name": "Goat Anti-Human IgG (0.1mg/mL)",
        "supplier": "Fisher Scientific",
        "catalog_number": "A18817",
        "cost_per_unit": 205.00, 
        "quantity": 10 #1mg at concentration of 2mg/ml, need it at 0.1mlg/ml, so 10 ml of diluted solution per vial, 10ml = 10000 ul
    },

    # "heat-inactivated_serum": {
    #     "name": "Heat-Inactivated Serum", #is FBS
    #             "supplier": "",
    #     "catalog_number": "",
    #     "cost_per_unit": 0, 
    #     "quantity": 1 #never purchased
    # },

    "hrp_conjugated_raabbit_antigoat_igg": {
        "name": "HRP Conjugated Rabbit Anti-Goat IgG (1:20,000)",
        "supplier": "Millipore Sigma",
        "catalog_number": "A5420",
        "cost_per_unit": 205.00, 
        "quantity": 20000 #1ml, need diluted to 1:20,000
    },

    "human_igg": {
        "name": "Human IgG (0.1mg/mL)",
        "supplier": "Millipore Sigma",
        "catalog_number": "I4506",
        "cost_per_unit": 281.00, 
        "quantity": 50/0.1 #50 mg in vial, need diluted to 0.1mg/ml, will call in ul, but this is ml
    },

    "human_serum": {
        "name": "Human Serum", #undiluted
        "supplier": "Millipore Sigma",
        "catalog_number": "H4522",
        "cost_per_unit": 120, 
        "quantity": 20
    },

    "human_serum_1:100": {
        "name": "Human Serum (1:100)",
        "supplier": "Millipore Sigma",
        "catalog_number": "H4522",
        "cost_per_unit": 270, 
        "quantity": 100*100 #100ml per bottle, diluted 1:100
    },

    
    "protein_ladder": {
        "name": "1 kb Protein Ladder",
        "supplier": "New England Biolabs",
        "catalog_number": "N3232S",
        "cost_per_unit": 62,
        "quantity": 0.5 #500ul=0.5ml
    },

    "rabbit_antisrbc_antiserum": {
        "name": "Rabbit Anti-RBC Antiserum",
        "supplier": "Rockland",
        "catalog_number": "213-4139",
        "cost_per_unit": 427, 
        "quantity": 5 # 50mg, reconstitued volume is 5ml, so 5000 ul
    },

    "rt_anti-digoxigenin_peroxidase": {
        "name": "RT Anti-Digoxigenin Peroxidase Conjugate Antibody",
        "supplier": "Millipore Sigma",
        "catalog_number": "11633716001", 
        "cost_per_unit": 407.00, #says 50 units, how much is a unit? I am going to estimate a total  of 200ul based on other prices of similar products
        "quantity": 0.2 #200ul= 0.2 ml
    },

    "salmonella_h_antiserum": {
        "name": "Salmonella H Antiserum",
        "supplier": "Bio-Rad",
        "catalog_number": "3561124",
        "cost_per_unit": 1560, 
        "quantity": 60*3 #comes in 3ml vials, 60 per box; need to call by ml
    },

    "salmonella_o_antiserum": {
        "name": "Salmonella O Antiserum",
        "supplier": "VWR",
        "catalog_number": "90002-044",
        "cost_per_unit": 281.02, 
        "quantity": 3 #comes in 3ml vials
    },

    "serum_w_complement": {
        "name": "Serum with Complement", #is Guinea Pig Complement, we will need to purchase, so add info then
        "supplier": "VWR",
        "catalog_number": "IC0855852", #pulled infor from VWR but i am not sure if this is the one we purchased
        "cost_per_unit": 58.87, #cost per 1ml
        "quantity": 1000 #converted to ul
    },

    "tdt_enzyme": {
        "name": "Terminal Deoxynucleotidyl Transferase (TdT)",
        "supplier": "VWR",
        "catalog_number": "80500-112",
        "cost_per_unit": 273.92, #pulled from VWR website, not sure if is the one we purchased
        "quantity": 155 ## 0.155ml, and is called in spreadsheet by ul, so is 155 ul
        #775 units of TdT; one unit is the amount of enzyme required to transfer 1.0nmol of dAMP from dATP to the 3' -OH terminus of d(A)50 in 60 minutes at 37 °C  
    },
}

#towbin transfer buffer
## 25 mM Tris, 192 mM glycine, 20% (v/v) methanol, 0.025–0.1% SDS (pH 8.3)
## Add 2.5–10 ml 10% SDS to 1 L buffer prepared above

#boratge buffered saline
## 0.17M borate solution and 0.12 M NACL (adjust pH 8.5 with NaOH)

#trypan blue stain
### agar, borate bufffered saline, and 0.1% tgrypan blue
#### figure out exact quantities and then make an entry with correct cost