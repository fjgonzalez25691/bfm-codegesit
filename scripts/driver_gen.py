# Import necessary libraries
import random
import pandas as pd
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
    "Sol, 1",
    "Luna, 2",
    "Prado, 3",
    "Flores, 4",
    "Mayor, 5",
    "Álamos, 6",
    "Río, 7",
    "Estrella, 8",
    "Montaña, 9",
    "Jardín, 10",
    "Castillo, 11",
    "España, 12",
    "Pinos, 13",
    "Fuente, 14",
    "Estaciones, 15",
    "Molino, 16",
    "Rosales, 17",
    "Paz, 18",
    "Amistad, 19",
    "Sauces, 20",
    "Sierra, 21",
    "Horizonte, 22",
    "Alba, 23",
    "Nieve, 24",
    "Olivos, 25",
    "Bosque, 26",
    "Mar, 27",
    "Cisnes, 28",
    "Águila, 29",
    "Roble, 30",
    "Encina, 31",
    "Primavera, 32",
    "Invierno, 33",
    "Tormenta, 34",
    "Naranjos, 35",
    "Palmeras, 36",
    "Faro, 37",
    "Puerto, 38",
    "Laureles, 39",
    "Brisa, 40",
    "Rocas, 41",
    "Lago, 42",
    "Almendro, 43",
    "Aromas, 44",
    "Libertad, 45",
    "Comercio, 46",
    "Mercado, 47",
    "Cielo, 48",
    "Tréboles, 49",
    "Aurora, 50"
]
cities = [
    "Madrid",
    "San Sebastián de los Reyes",
    "Pozuelo de Alarcón",
    "Majadahonda",
    "Las Rozas",
    "Boadilla del Monte",
    "Alcorcón",
    "Leganés",
    "Getafe",
    "Rivas-Vaciamadrid",
    "Coslada",
    "San Fernando de Henares",
    "Torrejón de Ardoz",
    "Paracuellos de Jarama",
    "Villaviciosa de Odón",
    "Tres Cantos",
    "Colmenar Viejo",
    "Pinto",
    "Valdemoro"
]

def generate_address():
    # Combine street,  and city
    street = random.choice(streets)
    number = random.randint(1, 300)

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

# Convert the data to a DataFrame
drivers_df = pd.DataFrame(data)

# Save the data as a CSV file in the current directory
csv_path_drivers = r"D:\cursos_de_informatica\Atlassian\enlaces_codegeist\drivers.csv"  # File path updated for Windows
drivers_df.to_csv(csv_path_drivers, index=False)  # Save the DataFrame as a CSV

print(f"CSV file saved at: {csv_path_drivers}")