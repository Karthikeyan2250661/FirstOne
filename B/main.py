##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

import hotel_management as hm
import customer as cs
import utility as ut

def main():
    
    ## Fill your code for getting user inputs, objects creation and display statements
    hotel_mgmt = hm.HotelManagement()
    
    num_rooms = int(input("Enter the number of rooms: "))
    for i in range(1, num_rooms + 1):
        room_detail = input(f"Enter the room details {i}:\n")
        details = room_detail.split(":")
        room_no = details[0]
        customer_name = details[1]
        room_type = details[2]
        entry_date = details[3]
        return_date = details[4]
        try:
            if ut.validate_room_type(room_type):
                hotel_mgmt.add_customer_details(room_no, customer_name, room_type, entry_date, return_date)
        except Exception as e:
            print(e)
    
    search_room_type = input("Enter the room type to be searched: ")
    customer_details = hotel_mgmt.view_customer_details(search_room_type)
    if not customer_details:
        print("No customers found")
    else:
        for detail in customer_details:
            print(f"Room number: {detail[0]}")
            print(f"Customer Name: {detail[1]}")
            print(f"Number Of Days: {detail[2]}")
            print(f"Total Amount: {detail[3]}")
    
    print("Customer Details In Sorted Order:")
    sorted_customers = hotel_mgmt.view_customers_sorted_by_name()
    for customer in sorted_customers:
        print(customer)

if __name__ == "__main__":
    main()

