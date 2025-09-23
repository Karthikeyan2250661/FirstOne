##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

class Customer:
    
    ## Define the parameterized constructor here
    def __init__(self, room_no, customer_name, room_type, entry_date, return_date):
        self._room_no = room_no
        self._customer_name = customer_name
        self._room_type = room_type
        self._entry_date = entry_date
        self._return_date = return_date
        self._no_of_days = 0
        self._total_cost = 0.0

    def get_room_no(self):
        return self._room_no
    
    def set_room_no(self, room_no):
        self._room_no = room_no
    
    def get_customer_name(self):
        return self._customer_name
    
    def set_customer_name(self, customer_name):
        self._customer_name = customer_name
    
    def get_room_type(self):
        return self._room_type
    
    def set_room_type(self, room_type):
        self._room_type = room_type
    
    def get_entry_date(self):
        return self._entry_date
    
    def set_entry_date(self, entry_date):
        self._entry_date = entry_date
        
    def get_return_date(self):
        return self._return_date
    
    def set_return_date(self, return_date):
        self._return_date = return_date
    
    def get_no_of_days(self):
        return self._no_of_days
    
    def set_no_of_days(self, no_of_days):
        self._no_of_days = no_of_days
    
    def get_total_cost(self):
        return self._total_cost
    
    def set_total_cost(self, total_cost):
        self._total_cost = total_cost
    
    ## Write __repr__ method here
    def __repr__(self):
        return f"Customer ({self._room_no}, {self._customer_name}, {self._room_type},{self._no_of_days},{self._total_cost})"
    
    def calculate_no_of_days(self):
        ## Fill your code here
        delta = self._return_date - self._entry_date
        self._no_of_days = delta.days
        return None
    
    def calculate_total_amount(self):
        ## Fill your code here
        room_rates = {
            "Single": 3000,
            "Double": 4000,
            "Triple": 5000,
            "Deluxe": 6000
        }
        
        rate = room_rates[self._room_type]
        base_cost = self._no_of_days * rate
        
        # For <=3 days: no discount (0%), for >3 days: room-specific discount
        if self._no_of_days <= 3:
            self._total_cost = base_cost
        else:
            if self._room_type == "Single":
                discount_percent = 13
            elif self._room_type == "Double":
                discount_percent = 15
            elif self._room_type == "Triple":
                discount_percent = 17
            elif self._room_type == "Deluxe":
                discount_percent = 19
            
            discount_amount = rate * (discount_percent / 100)
            self._total_cost = base_cost - discount_amount
        
        return None

