# utility.py
import re
import exception as ie
from datetime import datetime

def validatedate(bookingdate):
    try:
        # Check if date is in ddmmyyyy format
        if not re.match(r'^\d{8}$', bookingdate):
            raise ie.InvalidDateException("Invalid date format")
        # Try to parse the date to check if it's valid
        day = int(bookingdate[:2])
        month = int(bookingdate[2:4])
        year = int(bookingdate[4:8])
        datetime(year, month, day)
        return True
    except ie.InvalidDateException as e:
        return e.message
    except ValueError:
        return "Invalid date format"

def validateplace(place):
    try:
        valid_places = ["Beach", "Pilgrimage", "Heritage", "Hill Station", "Water Falls", "Adventures"]
        if place not in valid_places:
            raise ie.InvalidPlaceException("Invalid place")
        return True
    except ie.InvalidPlaceException as e:
        return e.message
