import os
import json

def combine_json_files(input_folder, output_folder, output_filename):
    # Ensure the output folder exists, create if not

    combined_data = []

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as file:
                data = json.load(file)
                combined_data.append(data)

    # Write combined data to a single JSON file
    with open(os.path.join(output_folder, output_filename), 'w') as outfile:
        json.dump(combined_data, outfile, indent=4)

# Example usage:
input_folder = r"D:\ict300001 flask final\final product\Final\result\final"
output_folder = r"D:\ict300001 flask final\flask-sb-admin-master reworked\apps\summary"
output_filename = r"dien_tu.json"

combine_json_files(input_folder, output_folder, output_filename)