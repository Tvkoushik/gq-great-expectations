import json
import csv
import requests
import os

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "London"}

headers = {
    "X-RapidAPI-Key": "be4d7396b7msh753fc596e82d2d8p139902jsn3e1a09a140bb",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

# Convert JSON response to a Python object
data = json.loads(response.content)

print(data)


# Flatten the dictionary
flattened_dict = {}


def flatten_dict(dictionary, prefix=""):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            flatten_dict(value, prefix + key + "_")
        else:
            flattened_dict[prefix + key] = value


flatten_dict(data)

# Write the flattened dictionary to a CSV file
filename = "./data/weather_data.csv"
write_header = False  # Flag to determine whether to write the header

# Check if the file already exists
file_exists = os.path.isfile(filename)

with open(filename, "a+", newline="") as file:
    writer = csv.writer(file)

    # Write the header only if the file doesn't exist
    if not file_exists:
        writer.writerow(flattened_dict.keys())
        write_header = True

    # Write the data row
    writer.writerow(flattened_dict.values())

if write_header:
    print("Header written successfully.")

print("Data appended successfully.")
