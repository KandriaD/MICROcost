# MICRO351L Biology of Microorganisms Laboratory
# 2.0 Credit Hours
# $125 Lab Fee
# Spring 2025 has 3 sectiions, for a total of 30 students

# Import libraries
from Libraries.bacteria import bacteria_list
from Libraries.media import media_list, standard_volumes_ml
from Libraries.supplies import supplies_list
from Libraries.chemicals import chemical_list
from Libraries.antibiotics import antibiotic_list

# Define the course details
students = 30
groups = 15 # 5 per section
lab_fee = 125

def calculate_experiment_cost(bacteria, media, number_of_samples, distribution_types):
    total_cost = 0

    # Cost calculation for biologicals (bacteria and media)
