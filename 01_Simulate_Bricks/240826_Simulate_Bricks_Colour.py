"""
Generating bricks incoming delivery, simulation of the scanning of the bricks

open task :
- only nurn number 1 for the first turn, the rest can be all the same number
"""

import csv
import random
import os
import colorsys

date = 240826

def generate_brick_data(num_bricks):
    cities = {
        "Augsburg": 79,
        "Starnberg": 28,
        "Ingolstadt": 84,
        "Erding": 43,
        "Rosenheim": 70,
        "Landshut": 73,
        "Fuerstenfeldebruck": 29,
        "Dachau": 30,
        "Garmisch-Partenkichen": 90,
        "Kempten": 123,
        "Donauwoerth": 116
    }
    
    brick_formats = {
        "Reichsformat": [250, 120, 65],
        "Normalformat": [240, 115, 71],
        "Duennformat": [240, 115, 52]
    }

    def generate_brick_nuances(base_colour, num_nuances):
        nuances = []

        r, g, b = [x/255.0 for x in base_colour]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        
        base_step = 0.8/ (num_nuances - 1)  # base step for vriation
        
        for i in range(num_nuances) :
            
            random_step = base_step * random.uniform(0.5, 1.5)
            
            changed_h = (h + random.uniform(-0.05, 0.05)) % 1.0
            changed_s = max(0.1, min(1.0, s + random.uniform(-0.1, 0.1)))
            changed_v = max(0.1, min(0.9, v + random_step * (i - (num_nuances-1)/2) + random.uniform(-0.1, 0.1)))
            
            # Converts back to RGB
            r, g, b = colorsys.hsv_to_rgb(changed_h, changed_s, changed_v)
            nuance = tuple(int(x * 255) for x in (r, g, b))
            nuances.append(nuance)
        
        return nuances
    
    def get_base_colour():
        base_colours = {
            "red-brown": (160, 75, 40),
            "light_red" : (220, 110, 100),
            "beige": (250, 200, 150),
            "grey": (180, 180, 180)
        }
        colour_name = random.choice(list(base_colours.keys()))
        return base_colours[colour_name], colour_name

    data = []
    delivery_number = 1
    total_bricks = 0

    while total_bricks < num_bricks:
        delivery_size = random.randint(1000, 2100)
        turn_1 = random.randint(210, 310)
        
        production_year = random.randint(1830, 1879) if random.random() <= 0.15 else random.randint(1880, 1960)
        city = random.choice(list(cities.keys()))
        distance = cities[city]

        brick_format = "Reichsformat"
        brick_dimensions = brick_formats[brick_format]
        brick_length = brick_dimensions[0]
        brick_width = brick_dimensions[1]
        brick_height = brick_dimensions[2]

        base_colour, colour_name = get_base_colour()
        nuances = generate_brick_nuances(base_colour, random.randint(9, 13))

        for i in range(delivery_size):
            turn_nr = 1 if i < turn_1 else 2

            if total_bricks >= num_bricks:
                break
            
            nuance = nuances[random.randint(0, len(nuances) - 1)]
            mortar_rests = round(random.uniform(0.05, 0.5), 2) if random.random() > 0.2 else round(random.uniform(0.01, 0.9), 1)
            colour_rests = round(random.uniform(0.07, 0.15), 2) if random.random() > 0.7 else 0.01

            if random.random() <= 0.2:
                lu = round(random.uniform((brick_length * 0.5), brick_length), 1)
            else:
                lu = round(random.uniform((brick_length * 0.95), (brick_length * 1.05)), 1)
                
            wu = round(random.uniform((brick_width * 0.95), (brick_width * 1.05)), 1)
            hu = round(random.uniform((brick_height * 0.95), (brick_height * 1.05)), 1)

            volume = round(lu * wu * hu, 1)
            volume_perfect = brick_length * brick_width * brick_height
            volume_percent = round(volume / volume_perfect, 2)

            delivery_data = {
                "brick_id": len(data) + 1,
                "delivery_nr": delivery_number,
                "brick_format": brick_format,
                "brick_original_dimensions (mm)" : f"{brick_length}, {brick_width}, {brick_height}",
                "brick_origin": city,
                "brick_distance (km)": distance,
                "age (y)": 2024 - production_year,
                "colour name": colour_name,
                "turn_nr": turn_nr, 
                "mortar rests (%)": mortar_rests,
                "colour rests (%)" : colour_rests,
                "R": nuance[0],
                "G": nuance[1],
                "B": nuance[2],
                "lu (mm)": lu,
                "wu (mm)": wu,
                "hu (mm)": hu,
                "volume (%)" : volume_percent
            }

            data.append(delivery_data)
            total_bricks += 1

        delivery_number += 1

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    num_bricks = 7000
    brick_data = generate_brick_data(num_bricks)

    output_directory = "C:\\Users\\david\\OneDrive\\Documents\\01_Architektur\\02_MA Architektur\\TUM\\2024_Sommersemester\\01_THESIS\\02_MA_Thesis\\02_Listing\\01_Visual_Studio\\240816_Simulation\\01_Simulate_Bricks"
    output_file = f"{date}_brick-colour_simulation.csv"

    output_path = os.path.join(output_directory, output_file)
    
    # Save data to CSV
    save_to_csv(brick_data, output_path)