#bacteria available for growth in all Micro Labs
#Define the bacteria_list dictionary

bacteria_list = {
    "Acinetobacter baumannii": {
        "synonym": ["A. baumannii"],
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
        "synonym": ["A. lwoffii"],
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
        "synonym": ["A. faecalis"],
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
        "synonym": ["A. niger"],
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
        "synonym": ["B. cereus"],
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
        "synonym": ["B. subtilis"],
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
        "synonym": ["B. bronchiseptica"],
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
        "synonym": ["B. cepacia"],
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
        "synonym": ["C. jenuni"],
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
        "synonym": ["C. albicans"],
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
        "synonym": ["C. tropicalis"],
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
        "synonym": ["C. freundii"],
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
        "synonym": ["C. sporogenes"],
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
        "synonym": ["C. diphtheriae"],
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
        "synonym": ["C. xerosis"],
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
        "synonym": ["E. tarda"],
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
        "synonym": ["E. meningoseptica"],
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
        "synonym": ["E. cloacae", "Klebsiella cloacae", "K. cloacae"],
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
        "synonym": ["E. faecalis"],
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
        "synonym": ["E. rhusiopathiae"],
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
        "synonym": ["E. coli"],
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
        "synonym": ["G. stearothermophilus"],
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
        "synonym": ["H. influenzae"],
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
        "synonym": ["H. parainfluenzae"],
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
        "synonym": ["H. salinarum"],
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
        "synonym": ["K. aerogenes", "E. aerogenes", "E. aerogenes"],
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
        "synonym": ["K. pneumoniae", "E. pneumoniae", "E. pneumoniae"],
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
        "synonym": ["K. rosea"],
        "gram": "positive",
        "shape": "cocci",
        "growth": "aerobic",
        "optimum_temperature": "37C",
        "optimum_pH": "7.0",
        "pathogenicity": "common in the throat",
        "notes": "common in the throat",
        "stock_cost": 0.00
    },

    "Lactococcus lactis": {
        "synonym": ["L. lactis"],
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
        "synonym": ["L. monocytogenes"],
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
        "synonym": ["M. luteus"],
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
        "synonym": ["M. catarrhalis"],
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
        "synonym": ["M. gordonae"],
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
        "synonym": ["M. smegmatis"],
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
        "synonym": ["N. gonorrhoeae"],
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
        "synonym": ["N. lactamica"],
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
        "synonym": ["N. meningitidis"],
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
        "synonym": ["N. sicca"],
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
        "synonym": ["P. notatum"],
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
        "synonym": ["P. hauseri", "P. vulgaris", "Proteus vulgaris"],
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
        "synonym": ["P. mirabilis"],
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
        "synonym": ["P. vulgaris"],
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
        "synonym": ["P. stuartii"],
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
        "synonym": ["P. aeruginosa"],
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
        "synonym": ["S. cerevisiae"],
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
        "synonym": ["S. enterica"],
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
        "synonym": ["S. enterica serovar enteriditis", "Salmonella enterica serotype enteriditis", "S. enterica enterica serovar enteriditis", "S. enteritidis"],
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
        "synonym": ["Salmonella enterica serotype typhimurium","S. enterica serovar typhimurium", "Salmonella enterica serotype typhimurium", "S. enterica enterica serovar typhimurium", "S. typhimurium"],
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
        "synonym": ["S. marcescens"],
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
        "synonym": ["S. dysenteriae"],
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
        "synonym": ["S. flexneri"],
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
        "synonym": ["S. sonnei"],
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
        "synonym": ["S. aureus"],
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
        "synonym": ["S. epidermidis"],
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
        "synonym": ["S. saprophyticus"],
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
        "synonym": ["S. maltophilia"],
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
        "synonym": ["S. agalactiae"],
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
        "synonym": ["S. gallolyticus", "S. bovis", "Streptococcus bovis"],
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
        "synonym": ["S. mitis"],
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
        "synonym": ["S. pneumoniae"],
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
        "synonym": ["S. pyogenes"],
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
        "synonym": ["V. alginolyticus"],
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
        "synonym": ["V. parahaemolyticus"],
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
        "synonym": ["Y. enterocolitica"],
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
