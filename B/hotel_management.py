##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

import customer as cs
import invalid_exception as ir
## Import necessary modules/packages here
import utility as ut

class HotelManagement:
    
    def __init__(self):
        self.customer_list = []
    
    def add_customer_details(self, room_no, customer_name, room_type, entry_date, return_date):
        ## Fill your code here
        entry_date_obj = ut.convert_date(entry_date)
        return_date_obj = ut.convert_date(return_date)
        customer = cs.Customer(room_no, customer_name, room_type, entry_date_obj, return_date_obj)
        customer.calculate_no_of_days()
        customer.calculate_total_amount()
        self.customer_list.append(customer)
        return None
    
    def view_customer_details(self, room_type):
        ## Fill your code here
        filtered_customers = []
        for customer in self.customer_list:
            if customer.get_room_type() == room_type:
                filtered_customers.append([
                    customer.get_room_no(),
                    customer.get_customer_name(),
                    customer.get_no_of_days(),
                    customer.get_total_cost()
                ])
        return filtered_customers
    
    def view_customers_sorted_by_name(self):
        ## Fill your code here
        sorted_customers = sorted(self.customer_list, key=lambda customer: customer.get_customer_name())
        return sorted_customers

