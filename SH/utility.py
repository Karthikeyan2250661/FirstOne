##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

import PasswordGeneration as pg

def generate_list(vehicle_list):
    ##Write your code here
    password_list = []
    for vehicle_entry in vehicle_list:
        model = vehicle_entry[0]
        reg_no = vehicle_entry[1]
        vehicle_type = vehicle_entry[2]
        if vehicle_type == '1':
            # Create Car object
            car = pg.Car(model, reg_no, vehicle_type)
            # Get generator and extract dictionary
            gen = car.generate_key()
            password_dict = next(gen)
            password_list.append(password_dict)
        elif vehicle_type == '2':
            # Create Bike object
            bike = pg.Bike(model, reg_no, vehicle_type)
            # Get generator and extract dictionary
            gen = bike.generate_key()
            password_dict = next(gen)
            password_list.append(password_dict)
    return password_list

def read_file(file):
    ##Write your code here
    vehicle_details = []
    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(',')
                    if len(parts) == 3:
                        model = parts[0].strip()
                        reg_no = parts[1].strip()
                        vehicle_type = parts[2].strip()
                        vehicle_details.append([model, reg_no, vehicle_type])
    except FileNotFoundError:
        print(f"Error: File {file} not found")
        return []
    return vehicle_details

def check_password(reg_no, password, password_list):
    ##Write your code here
    for password_dict in password_list:
        if reg_no in password_dict:
            if password_dict[reg_no] == password:
                return True
    return False
