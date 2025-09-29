# touristservice.py
import tourist as ps

class Tourism:
    def __init__(self):
        self.touristlist = []

    def generateid(self, touristname, bookingdate):
        first_char = touristname[0].upper()
        last_char = touristname[-1].upper()
        month = bookingdate[2:4]
        year = bookingdate[6:8]
        tourist_id = first_char + last_char + month + year
        return tourist_id

    def addtouristdetails(self, touristid, touristname, place, bookingdate, noofdays, nooftickets):
        tourist = ps.Tourist(touristid, touristname, place, bookingdate, noofdays, nooftickets)
        tourist.calculatebillamount()
        self.touristlist.append(tourist)

    def retrievedetailsbyplace(self, place):
        tourists_by_place = []
        for tourist in self.touristlist:
            if tourist.getplace() == place:
                tourists_by_place.append(tourist)
        if len(tourists_by_place) == 0:
            return "No tourists found"
        else:
            return tourists_by_place

    def searchtouristbymonth(self, month):
        tourists_by_month = []
        for tourist in self.touristlist:
            tourist_month = int(tourist.getbookingdate()[2:4])
            if tourist_month == month:
                tourist_dict = {
                    "touristid": tourist.gettouristid(),
                    "touristname": tourist.gettouristname(),
                    "place": tourist.getplace(),
                    "bookingdate": tourist.getbookingdate()
                }
                tourists_by_month.append(tourist_dict)
        if len(tourists_by_month) == 0:
            return "No tourists found"
        else:
            return tourists_by_month
