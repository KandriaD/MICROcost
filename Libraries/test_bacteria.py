# test_bacteria.py
# test_bacteria.py

print("Starting test...")

# Try to import bacteria_list from bacteria.py
try:
    from bacteria import bacteria_list
    print("Bacteria dictionary imported successfully.")
except Exception as e:
    print(f"Error importing bacteria_list: {e}")

# Print the whole dictionary to check if it's loaded correctly
print("Printing bacteria dictionary...")
if 'bacteria_list' in locals():
    print(bacteria_list)
else:
    print("bacteria_list not found.")

# Test individual entries in the dictionary
print("Printing synonyms for Escherichia coli...")
if "Escherichia coli" in bacteria_list:
    print(bacteria_list["Escherichia coli"]["synonyms"])
else:
    print("Escherichia coli not found in dictionary.")