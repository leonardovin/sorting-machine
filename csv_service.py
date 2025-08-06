import csv

COLUMNS = [
    "Width",
    "Height",
    "Length",
    "Mass"
]



def clean_values(value):
    if value == "":
        return None
    # try to extract the number from the value
    try:
        return float(value)
    except ValueError:
        return None

def validate_number_input(value):
    print(f"Validating number input: {value}")
    if value is None:
        return None
    if float(value) <= 0:
        return None
    
    return value


def get_positive_number(value):
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None
    
def validate_value_input(value):
    cleaned_value = clean_values(value)
    if cleaned_value is None:
        return None
    validated_value = validate_number_input(cleaned_value)
    if validated_value is None:
        return None
    return get_positive_number(validated_value)


class CSVService:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        with open(self.file_path, 'r') as file:
            try:
                reader = csv.reader(file)
                data = []
                total_rows = 0
                
                for row in reader:
                    total_rows += 1
                    # Skip rows that don't have enough columns
                    if len(row) < 4:
                        print(f"Skipping row: {row}")
                        continue
                        
                    # skip the first row
                    if row[0] == "width":

                        continue
                    
                    width = validate_value_input(row[0])
                    height = validate_value_input(row[1])
                    length = validate_value_input(row[2])
                    mass = validate_value_input(row[3])
                    
                    if width is None or height is None or length is None or mass is None:
                        continue
                    
                    data.append({
                        "width": width,
                        "height": height,
                        "length": length,
                        "mass": mass
                    })
                
                
                return data, total_rows
            except Exception as e:
                print(f"Error reading CSV file: {e}")
                return None
    
    
        