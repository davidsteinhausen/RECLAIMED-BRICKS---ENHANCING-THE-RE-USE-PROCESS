import csv
import json


input_csv_path = f"C:\\Users\\david\\OneDrive\\Documents\\01_Architektur\\02_MA Architektur\\TUM\\2024_Sommersemester\\01_THESIS\\02_MA_Thesis\\02_Listing\\01_Visual_Studio\\240816_Simulation\\01_Simulate_Bricks\\240826_brick-colour_simulation.csv"
output_json_path = "240826_brick-colour_simulation.json" 

def csv_to_json(csv_file_path, json_file_path):
 
    bricks_data = []


    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
       
        for row in csv_reader:
          
            for key, value in row.items():
                try:
             
                    row[key] = float(value)
             
                    if row[key].is_integer():
                        row[key] = int(row[key])
                except ValueError:
     
                    pass
            
    
            bricks_data.append(row)

    # Write json
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(bricks_data, json_file, indent=2)

    print(f"Conversion complete. JSON file saved as {json_file_path}")


csv_to_json(input_csv_path, output_json_path)