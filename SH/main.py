##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

import utility as ut

def main():
    ## Write your code here for invoking functions, getting inputs and displaying the output.
    # Step 1: Read vehicle details from file
    vehicle_details = ut.read_file("VehicleDetails.txt")
    # Step 2: Generate password list
    password_list = ut.generate_list(vehicle_details)
    # Step 3: Get user inputs
    reg_no = input("Enter registration no.: ")
    password = input("Enter password: ")
    # Step 4: Check password
    result = ut.check_password(reg_no, password, password_list)
    # Step 5: Display result
    if result:
        print("Access granted")
    else:
        print("Incorrect registration number or password")
    return

if __name__ == "__main__":
    main()
