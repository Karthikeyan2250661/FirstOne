# tourist.py
class Tourist:
    def __init__(self, touristid, touristname, place, bookingdate, noofdays, nooftickets):
        self.__touristid = touristid
        self.__touristname = touristname
        self.__place = place
        self.__bookingdate = bookingdate
        self.__noofdays = noofdays
        self.__nooftickets = nooftickets
        self.__billamount = 0.0

    def gettouristid(self):
        return self.__touristid

    def settouristid(self, touristid):
        self.__touristid = touristid

    def gettouristname(self):
        return self.__touristname

    def settouristname(self, touristname):
        self.__touristname = touristname

    def getplace(self):
        return self.__place

    def setplace(self, place):
        self.__place = place

    def getbookingdate(self):
        return self.__bookingdate

    def setbookingdate(self, bookingdate):
        self.__bookingdate = bookingdate

    def getnoofdays(self):
        return self.__noofdays

    def setnoofdays(self, noofdays):
        self.__noofdays = noofdays

    def getnooftickets(self):
        return self.__nooftickets

    def setnooftickets(self, nooftickets):
        self.__nooftickets = nooftickets

    def getbillamount(self):
        return self.__billamount

    def setbillamount(self, billamount):
        self.__billamount = billamount

    def calculatebillamount(self):
        prices = {
            "Beach": 270,
            "Pilgrimage": 350,
            "Heritage": 430,
            "Hill Station": 780,
            "Water Falls": 1200,
            "Adventures": 4500
        }
        price_per_ticket = prices.get(self.__place, 0)
        self.__billamount = price_per_ticket * self.__noofdays * self.__nooftickets
        return self.__billamount
