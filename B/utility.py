##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

import invalid_exception as ir
from datetime import datetime, date

def validate_room_type(room_type):
    try:
        ## Fill your code here
        valid_room_types = ["Single", "Double", "Triple", "Deluxe"]
        if room_type in valid_room_types:
            return True
        else:
            raise ir.InvalidRoomTypeException("Invalid Room Type")
    except ir.InvalidRoomTypeException as e:
        ## Fill your code here
        raise e

def convert_date(str_date):
    ## Write your code here
    date_obj = datetime.strptime(str_date, "%d/%m/%Y").date()
    return date_obj

