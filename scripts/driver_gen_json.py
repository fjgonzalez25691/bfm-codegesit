# ==============================================================
# Script: driver_gen_json.py
# Description:
#   This script generates random driver data for the Boltium Fleet
#   Manager project. The generated data includes names, addresses,
#   and other non-sensitive information.
#
# Key Notes:
# - All data is fictitious and randomly generated.
# - No real or confidential data is used in any form.
# - The script adheres to strict ethical and legal standards.
# ==============================================================



# Import necessary libraries
import random
import pandas as pd
import json
from datetime import datetime

# Generate random names
spanish_first_names = [
    "Juan", "María", "José", "Ana", "Luis", "Carmen", "Francisco", "Isabel", 
    "Antonio", "Marta", "Javier", "Lucía", "Carlos", "Sofía", "Manuel", 
    "Clara", "Diego", "Elena", "Miguel", "Raquel", "Álvaro", "Laura", 
    "Pablo", "Teresa", "Alejandro"
]

spanish_last_names = [
    "García", "Martínez", "López", "Sánchez", "González", "Pérez", "Hernández", 
    "Rodríguez", "Fernández", "Moreno", "Jiménez", "Ruiz", "Álvarez", "Torres", 
    "Romero", "Díaz", "Navarro", "Vega", "Domínguez", "Gil", "Castro", 
    "Ortiz", "Rubio", "Molina", "Serrano", "Blanco", "Suárez", "Méndez", 
    "Ramos", "Santos", "Iglesias", "Crespo", "Aguilar", "Vázquez", "Carrasco", 
    "Reyes", "Ortega", "Delgado", "Marín", "Cano", "Prieto", "Peña", 
    "Calvo", "Rojas", "Luna", "Campos", "Pascual", "Soler", "Guzmán", "Santana"
]

def generate_full_name():
    # Combine first name with two last names
    return f"{random.choice(spanish_first_names)} {random.choice(spanish_last_names)} {random.choice(spanish_last_names)}"

# Generate ages between 25 and 65 using a normal distribution
def generate_age():
    age = int(random.gauss(45, 10))  # Mean 45, standard deviation 10
    return min(max(age, 25), 65)  # Ensure the age is within 25-65

# Generate random National ID (DNI in Spain)
def generate_national_id():
    dni_number = random.randint(10000000, 99999999)
    dni_letters = "TRWAGMYFPDXBNJZSQVHLCKE"  # Valid letters for DNI
    letter = dni_letters[dni_number % 23]
    return f"{dni_number}{letter}"

# Generate random addresses
streets = [
    "Sol, 1", "Luna, 2", "Prado, 3", "Flores, 4", "Mayor, 5", 
    "Álamos, 6", "Río, 7", "Estrella, 8", "Montaña, 9", "Jardín, 10"
]
cities = [
    "Madrid", "San Sebastián de los Reyes", "Pozuelo de Alarcón", 
    "Majadahonda", "Las Rozas", "Boadilla del Monte", "Alcorcón", 
    "Leganés", "Getafe", "Rivas-Vaciamadrid"
]

def generate_address():
    # Combine street and city
    street = random.choice(streets)
    city = random.choice(cities)
    return f"{street}, {city}"

# Generate random driving license numbers
def generate_driving_license():
    categories = ["B", "B+E", "C", "C+E", "D"]
    license_number = random.randint(100000000, 999999999)
    category = random.choice(categories)
    return f"{license_number} ({category})"

# Create a DataFrame for 270 drivers
data = {
    "Driver_ID": [f"C{str(i).zfill(3)}" for i in range(1, 271)],
    "Full_Name": [generate_full_name() for _ in range(270)],
    "Date_of_Birth": [
        (datetime.now().year - generate_age()) for _ in range(270)
    ],
    "National_ID": [generate_national_id() for _ in range(270)],
    "Address": [generate_address() for _ in range(270)],
    "Phone": [f"6{random.randint(10000000, 99999999)}" for _ in range(270)],
    "Hire_Date": ["2025-01-01" for _ in range(270)],
    "Driving_License": [generate_driving_license() for _ in range(270)],
}

# Convert the data to a list of dictionaries for JSON
drivers_json = pd.DataFrame(data).to_dict(orient="records")

# Save the JSON file in the current directory
json_path = r"D:\cursos_de_informatica\Atlassian\enlaces_codegeist\drivers.json"  # File path updated for Windows
with open(json_path, "w") as json_file:
    json.dump(drivers_json, json_file, indent=4)

print(f"JSON file saved at: {json_path}")
