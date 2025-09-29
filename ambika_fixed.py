from enum import Enum
from abc import ABC, abstractmethod
import sys

# Define the Category enum
class Category(Enum):
    FICTION = "FICTION"
    NON_FICTION = "NON_FICTION"
    EDUCATIONAL = "EDUCATIONAL"
    HOME_APPLIANCES = "HOME_APPLIANCES"
    COMPUTERS = "COMPUTERS"
    MOBILES = "MOBILES"

# Define the Discountable interface
class Discountable(ABC):
    @abstractmethod
    def apply_discount(self):
        pass

# Define the abstract InventoryItem class
class InventoryItem(Discountable):
    def __init__(self, name, price, quantity_in_stock, category):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.category = category
    
    def restock(self, quantity):
        self.quantity_in_stock += quantity
        print(f"Restocked {quantity} units of {self.name}")
    
    def sell(self, quantity):
        self.quantity_in_stock -= quantity
        print(f"Sold {quantity} units of {self.name}")
    
    def display_info(self):
        print(f"Item: {self.name}")
        print(f"Category: {self.category.value}")
        print(f"Base Price: ${self.price}")
        print(f"Stock Level: {self.quantity_in_stock}")
    
    @abstractmethod
    def calculate_price(self):
        pass
    
    def apply_discount(self):
        return self.calculate_price()

# Define the Book class
class Book(InventoryItem):
    def __init__(self, name, price, quantity_in_stock, category, author, isbn):
        super().__init__(name, price, quantity_in_stock, category)
        self.author = author
        self.isbn = isbn
    
    def get_author(self):
        return self.author
    
    def get_isbn(self):
        return self.isbn
    
    def calculate_price(self):
        # Apply 10% discount
        return self.price * 0.9

# Define the ElectronicItem class
class ElectronicItem(InventoryItem):
    def __init__(self, name, price, quantity_in_stock, category, warranty_months, brand):
        super().__init__(name, price, quantity_in_stock, category)
        self.warranty_months = warranty_months
        self.brand = brand
    
    def get_warranty_months(self):
        return self.warranty_months
    
    def get_brand(self):
        return self.brand
    
    def calculate_price(self):
        # Apply 20% discount
        return self.price * 0.8

#Non editable starts here
def main():
    input_data = sys.stdin.read().splitlines()
    
    item_type = input_data[0]
    name = input_data[1]
    base_price = float(input_data[2])
    quantity_in_stock = int(input_data[3])
    category_str = input_data[4].upper()
    
    try:
        category = Category[category_str]
    except KeyError:
        print("Invalid category entered.")
        return
    
    item = None
    
    if item_type.lower() == "book":
        author = input_data[5]
        isbn = input_data[6]
        item = Book(name, base_price, quantity_in_stock, category, author, isbn)
    elif item_type.lower() == "electronic":
        warranty_months = int(input_data[5])
        brand = input_data[6]
        item = ElectronicItem(name, base_price, quantity_in_stock, category, warranty_months, brand)
    else:
        print("Invalid item type entered.")
        return
    
    action = input_data[7]
    quantity = int(input_data[8])
    
    if action.lower() == "sell":
        item.sell(quantity)
    elif action.lower() == "restock":
        item.restock(quantity)
    else:
        print("Invalid action.")
        return
    
    item.display_info()
    if action.lower() == "sell":
        print(f"New Price: ${item.calculate_price():.2f}")

if __name__ == "__main__":
    main()
#Non editable ends here
