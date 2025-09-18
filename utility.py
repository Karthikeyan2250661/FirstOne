
from datetime import date
import exception as ie
import re

def read_file(file):
    records = []
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(line)
    except FileNotFoundError:
        print(f"File {file} not found")
        return []
    return records

def validate_request_id(request_id):
    try:
        pattern = r"^R0\d{2}$"
        if not re.match(pattern, request_id):
            raise ie.InvalidRequestIdException("Invalid Request Id")
        return True
    except ie.InvalidRequestIdException as e:
        return e.message

def convert_date(str_date):
    year, month, day = map(int, str_date.split("-"))
    return date(year, month, day)
