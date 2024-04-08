import time
import re

js_file_path = 'chart-pie-demo.js'
data_file_path = 'b.txt'

# Function to update the data values in the JavaScript code
def update_data_values(js_code, data_values):
    # Define regular expressions to find and replace the data values within datasets
    data_regex = r'data:\s*\[([\d.,\s]+)\]\s*'
    updated_code = re.sub(data_regex, f'data: {str(data_values)}', js_code)

    return updated_code

# Loop to update the JavaScript code every 1 second
while True:
    # Read the data from the file
    with open(data_file_path, 'r') as file:
        data = file.read().strip()

    # Split the data into individual values
    data_values = [float(value) for value in data.split(',')]

    # Read the JavaScript code from the file
    with open(js_file_path, 'r') as file:
        js_code = file.read()

    # Update the data values in the JavaScript code
    updated_js_code = update_data_values(js_code, data_values)

    # Write the updated JavaScript code back to the file
    with open(js_file_path, 'w') as file:
        file.write(updated_js_code)

    time.sleep(1)
