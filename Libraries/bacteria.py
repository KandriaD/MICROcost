#bacteria available for growth in all Micro Labs
#Define the bacteria_list dictionary

bacteria_list = {
    "Acinetobacter baumannii": {
        "synonyms": ["A. baumannii"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Actinetobacter lwoffii": {
        "synonyms": ["A. lwoffii"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Alcaligenes faecalis": {
        "synonyms": ["A. faecalis"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Aspergillus niger": {
        "synonyms": ["A. niger"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Bacillus cereus": {
        "synonyms": ["B. cereus"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in rice",
        "stock_cost": 0.00
    },

    "Bacillus subtilis": {
        "synonyms": ["B. subtilis"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in soil",
        "notes": "common in the environment",
        "stock_cost": 0.00
    },

    "Bordetella bronchiseptica": {
        "synonyms": ["B. bronchiseptica"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of kennel cough",
        "notes": "common in dogs",
        "stock_cost": 0.00
    },

    "Burkholderia cepacia": {
        "synonyms": ["B. cepacia"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Campylobacter jenuni": {
        "synonyms": ["C. jenuni"],
        "gram": "negative",
        "shape": "spiral",
        "growth": "microaerophilic",
        "optimum_temperature": "42C",
        "optimum_pH": "7.5",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in poultry",
        "stock_cost": 0.00
    },

    "Canidia albicans": {
        "synonyms": ["C. albicans"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of yeast infections",
        "notes": "",
        "stock_cost": 0.00
    },

    "Canidia tropicalis": {
        "synonyms": ["C. tropicalis"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of yeast infections",
        "notes": "",
        "stock_cost": 0.00
    },

    "Citrobacter freundii": {
        "synonyms": ["C. freundii"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Clostridium sporogenes": {
        "synonyms": ["C. sporogenes"],
        "gram": "positive",
        "shape": "rod",
        "growth": "anaerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in soil",
        "notes": "common in the environment",
        "stock_cost": 0.00
    },

    "Corynebacterium diphtheriae": {
        "synonyms": ["C. diphtheriae"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of diphtheria",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Corynebacterium xerosis": {
        "synonyms": ["C. xerosis"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Edwardsiella tarda": {
        "synonyms": ["E. tarda"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in fish",
        "stock_cost": 0.00
    },

    "Elizabethkingia meningoseptica": {
        "synonyms": ["E. meningoseptica"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Enterobacter cloacae": {
        "synonyms": ["E. cloacae", "Klebsiella cloacae", "K. cloacae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Enterococcus faecalis": {
        "synonyms": ["E. faecalis"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Erysipelothrix rhusiopathiae": {
        "synonyms": ["E. rhusiopathiae"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of erysipelas",
        "notes": "common in pigs",
        "stock_cost": 0.00
    },

    "Escherichia coli": {
        "synonyms": ["E. coli"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of urinary tract infections",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Geobacillus stearothermophilus": {
        "synonyms": ["G. stearothermophilus"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "55C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in soil",
        "notes": "common in the environment",
        "stock_cost": 0.00
    },

    "Haemophilus influenzae": {
        "synonyms": ["H. influenzae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of respiratory infections",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Haeomphilus parainfluenzae": {
        "synonyms": ["H. parainfluenzae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Halobacterium salinarum": {
        "synonyms": ["H. salinarum"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in salt flats",
        "notes": "common in salt flats",
        "stock_cost": 0.00
    },

    "Klebsiella aerogenes": {
        "synonyms": ["K. aerogenes", "E. aerogenes", "E. aerogenes"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Klebsiella pneumoniae": {
        "synonyms": ["K. pneumoniae", "E. pneumoniae", "E. pneumoniae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of pneumonia",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Kocuria rosea": {
        "synonyms": ["K. rosea"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Lactocoocus lactis": {
        "synonyms": ["L. lactis"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Listeria monocytogenes": {
        "synonyms": ["L. monocytogenes"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in dairy",
        "stock_cost": 0.00
    },

    "Micrococcus luteus": {
        "synonyms": ["M. luteus"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the skin",
        "notes": "common in the skin",
        "stock_cost": 0.00
    },

    "Moraxella catarrhalis": {
        "synonyms": ["M. catarrhalis"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of respiratory infections",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Mycrobacterium gordonae": {
        "synonyms": ["M. gordonae"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in soil",
        "notes": "common in the environment",
        "stock_cost": 0.00
    },

    "Mycobacterium smegmatis": {
        "synonyms": ["M. smegmatis"],
        "gram": "positive",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in soil",
        "notes": "common in the environment",
        "stock_cost": 0.00
    },

    "Neisseria gonorrhoeae": {
        "synonyms": ["N. gonorrhoeae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of gonorrhea",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Neisseria lactamica": {
        "synonyms": ["N. lactamica"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Neisseria meningitidis": {
        "synonyms": ["N. meningitidis"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of meningitis",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Neisseria sicca": {
        "synonyms": ["N. sicca"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Penicillium notatum": {
        "synonyms": ["P. notatum"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of yeast infections",
        "notes": "",
        "stock_cost": 0.00
    },

    "Proteus hauseri": {
        "synonyms": ["P. hauseri", "P. vulgaris", "Proteus vulgaris"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Proteus mirabilis": {
        "synonyms": ["P. mirabilis"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Proteus vulgaris": {
        "synonyms": ["P. vulgaris"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Providencia stuartii": {
        "synonyms": ["P. stuartii"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Pseudomonas aeruginosa": {
        "synonyms": ["P. aeruginosa"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Saccharomyces cerevisiae": {
        "synonyms": ["S. cerevisiae"],
        "gram": "negative",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of yeast infections",
        "notes": "",
        "stock_cost": 0.00
    },

    "Salmonella enterica": {
        "synonyms": ["S. enterica"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in poultry",
        "stock_cost": 0.00
    },

    "Salmonella enterica enterica serovar enteriditis": {
        "synonyms": ["S. enterica serovar enteriditis", "Salmonella enterica serotype enteriditis", "S. enterica enterica serovar enteriditis", "S. enteritidis"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in poultry",
        "stock_cost": 0.00
    },

    "Salmonella enterica enterica serovar typhimurium": {
        "synonyms": ["S. enterica serovar typhimurium", "Salmonella enterica serotype typhimurium", "S. enterica enterica serovar typhimurium", "S. typhimurium"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in poultry",
        "stock_cost": 0.00
    },

    "Serratia marcescens": {
        "synonyms": ["S. marcescens"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Shigella dysenteriae": {
        "synonyms": ["S. dysenteriae"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of dysentery",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Shigella flexneri": {
        "synonyms": ["S. flexneri"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of dysentery",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Shigella sonnei": {
        "synonyms": ["S. sonnei"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of dysentery",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Staphylococcus aureus": {
        "synonyms": ["S. aureus"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of skin infections",
        "notes": "common in the skin",
        "stock_cost": 0.00
    },

    "Staphylococcus epidermidis": {
        "synonyms": ["S. epidermidis"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the skin",
        "notes": "common in the skin",
        "stock_cost": 0.00
    },

    "Staphylococcus saprophyticus": {
        "synonyms": ["S. saprophyticus"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the skin",
        "notes": "common in the skin",
        "stock_cost": 0.00
    },

    "Stenorophomonas maltophilia": {
        "synonyms": ["S. maltophilia"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of nosocomial infections",
        "notes": "common in hospitals",
        "stock_cost": 0.00
    },

    "Streptococcus agalactiae": {
        "synonyms": ["S. agalactiae"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of neonatal infections",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Streptococcus gallolyticus": {
        "synonyms": ["S. gallolyticus", "S. bovis", "Streptococcus bovis"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the gut",
        "notes": "common in the gut",
        "stock_cost": 0.00
    },

    "Streptococcus mitis": {
        "synonyms": ["S. mitis"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Streptococcus pneumoniae": {
        "synonyms": ["S. pneumoniae"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of pneumonia",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Streptococcus pyogenes": {
        "synonyms": ["S. pyogenes"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of strep throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Virbrio alginolyticus": {
        "synonyms": ["V. alginolyticus"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in fish",
        "stock_cost": 0.00
    },

    "Vibrio parahaemolyticus": {
        "synonyms": ["V. parahaemolyticus"],
        "gram": "negative",
        "shape": "rod",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in fish",
        "stock_cost": 0.00
    },
    
    "Yersinia enterocolitica": {
        "synonyms": ["Y. enterocolitica"],
        "gram": "negative",
        "shape": "rod",
        "growth": "facultative anaerobe",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "major cause of foodborne illness",
        "notes": "common in pork",
        "stock_cost": 0.00
    }
}
