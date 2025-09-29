# exception.py
class InvalidPlaceException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidDateException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
