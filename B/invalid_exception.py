##DO NOT CHANGE THE GIVEN TEMPLATE. WRITE YOUR CODE IN THE PROVIDED PLACES ALONE.

class InvalidRoomTypeException(Exception):
    message = ""
    
    ## Create the constructor here
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

