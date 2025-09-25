##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

## Import necessary modules here
from abc import ABC, abstractmethod

class Vehicle(ABC):
    ## Write your code here
    def __init__(self, model, reg_no, vehicle_type):
        self.__model = model
        self.__reg_no = reg_no
        self.__vehicle_type = vehicle_type
    
    # Getter methods for all attributes
    def get_model(self):
        return self.__model
    
    def get_reg_no(self):
        return self.__reg_no
    
    def get_vehicle_type(self):
        return self.__vehicle_type
    
    @abstractmethod
    def generate_key(self):
        pass

##Define the inherited class 'Car' here
class Car(Vehicle):
    def __init__(self, model, reg_no, vehicle_type):
        super().__init__(model, reg_no, vehicle_type)
    
    def generate_key(self):
        reg_no = self.get_reg_no()
        # Position-weighted ASCII sum for alphabets
        position_weighted_ascii = sum(ord(char) * i for i, char in enumerate(reg_no) if char.isalpha())
        # Get digits in sequence
        digits = [int(d) for d in reg_no if d.isdigit()]
        # Subtract 2nd and 3rd digits (if they exist)
        subtract_value = 0
        if len(digits) >= 2:
            subtract_value += digits[1]  # 2nd digit
        if len(digits) >= 3:
            subtract_value += digits[2]  # 3rd digit
        password = position_weighted_ascii - subtract_value
        # Return as generator (as specified in requirements)
        yield {reg_no: str(password)}

##Define the inherited class 'Bike' here
class Bike(Vehicle):
    def __init__(self, model, reg_no, vehicle_type):
        super().__init__(model, reg_no, vehicle_type)
    
    def generate_key(self):
        reg_no = self.get_reg_no()
        # Position-weighted ASCII sum for alphabets
        position_weighted_ascii = sum(ord(char) * i for i, char in enumerate(reg_no) if char.isalpha())
        # Get digits in sequence
        digits = [int(d) for d in reg_no if d.isdigit()]
        # Add first and last digits (different from car)
        add_value = 0
        if len(digits) >= 1:
            add_value += digits[0]   # First digit
        if len(digits) >= 2:
            add_value += digits[-1]  # Last digit
        password = position_weighted_ascii + add_value
        # Return as generator (as specified in requirements)
        yield {reg_no: str(password)}
