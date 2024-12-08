# Randomly generates vehicles script
# ==============================================================
# Script: vehicle_gen.py
# Description:
#   This script generates random vehicle data for the Boltium Fleet
#   Manager project. The generated data is based on predefined
#   specifications for the fictional Zinca 1000 model.
#
# Key Notes:
# - All vehicle data is fictitious and derived from publicly available
#   information, such as manufacturer specifications.
# - No real or confidential data is used in any form.
# - The script adheres to strict ethical and legal standards to ensure
#   transparency and compliance with data handling guidelines.
#
# Usage:
# - This script creates a JSON file containing the data for the fleet vehicles.
# ==============================================================

import os
import random
import json
from datetime import datetime

# Number of vehicles
num_vehicles = 90

# Define vehicle model and color
model = "Zinca 1000"
color = "Negro"

# Generate random license plates
def generate_plate():
    letters = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
    numbers = "".join(random.choices("0123456789", k=4))
    return f"{numbers}-{letters}"

# Generate random VIN
def generate_vin():
    return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=17))

# Generate data for vehicles
vehicles_data = []
for i in range(1, num_vehicles + 1):
    vehicle = {
        "Vehicle_ID": f"V{str(i).zfill(3)}",
        "Model": model,
        "Plate_Number": generate_plate(),
        "VIN": generate_vin(),
        "Purchase_Date": "2025-01-01",
        "Color": color
    }
    vehicles_data.append(vehicle)

# Save the data as a JSON file
json_path = os.path.join("..", "boltium_fleet_manager", "data", "vehicles.json")  
with open(json_path, "w") as json_file:
    json.dump(vehicles_data, json_file, indent=4)

print(f"JSON file saved at: {json_path}")
