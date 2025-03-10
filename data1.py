import json

# Create the data dictionary
data = {
    'name': 'Sara Smith',
    'age': 26,
    'City': 'Seattle, WA',  
    'interests': ['swimming', 'music', 'cooking'],
    'is_student': True  
}

# Open a file to write the JSON data
with open('data1.json', 'w') as json_file:
    # Dump the data dictionary into the JSON file
    json.dump(data, json_file, indent=4)

print("Data has been written to data1.json")
