# main.py
import touristservice as ts
import utility as ut

def parse_tourist_input(input_data):
    valid_places = ["Beach", "Pilgrimage", "Heritage", "Hill Station", "Water Falls", "Adventures"]
    place = None
    place_start = -1
    place_end = -1
    for valid_place in valid_places:
        if valid_place in input_data:
            place_start = input_data.find(valid_place)
            place_end = place_start + len(valid_place)
            place = valid_place
            break
    if place is None:
        return None, None, None, None, None
    touristname = input_data[:place_start]
    remaining = input_data[place_end:]
    digits = ''.join([c for c in remaining if c.isdigit()])
    if len(digits) < 10:
        return None, None, None, None, None
    bookingdate = digits[:8]
    days_tickets = digits[8:]
    if len(days_tickets) == 2:
        noofdays = int(days_tickets[0])
        nooftickets = int(days_tickets[1])
    elif len(days_tickets) == 3:
        option1_days = int(days_tickets[0])
        option1_tickets = int(days_tickets[1:])
        option2_days = int(days_tickets[:2])
        option2_tickets = int(days_tickets[2])
        if option2_days <= 20 and option2_tickets >= 1:
            noofdays = option2_days
            nooftickets = option2_tickets
        else:
            noofdays = option1_days
            nooftickets = option1_tickets
    else:
        noofdays = int(days_tickets[:-1])
        nooftickets = int(days_tickets[-1:])
    return touristname, place, bookingdate, noofdays, nooftickets

def main():
    no_tourists = int(input("Enter the number of registrations: "))
    tr = ts.Tourism()
    for i in range(0, no_tourists):
        print("Enter the registration details", i+1)
        input_data = input()
        result = parse_tourist_input(input_data)
        if result[0] is None:
            print("Invalid input format")
            continue
        touristname, place, bookingdate, noofdays, nooftickets = result
        place_status = ut.validateplace(place)
        if place_status != True:
            print(place_status)
            continue
        date_status = ut.validatedate(bookingdate)
        if date_status != True:
            print(date_status)
            continue
        touristid = tr.generateid(touristname, bookingdate)
        tr.addtouristdetails(touristid, touristname, place, bookingdate, noofdays, nooftickets)
    place = input("Enter the Place to be searched: ")
    place_status = ut.validateplace(place)
    if place_status == True:
        tourist_place = tr.retrievedetailsbyplace(place)
        if type(tourist_place) != str and tourist_place != None:
            for i in tourist_place:
                print("Tourist ID:", i.gettouristid())
                print("Tourist Name:", i.gettouristname())
                print("Number Of Days:", i.getnoofdays())
                print("Number Of Tickets:", i.getnooftickets())
                print("Bill Amount:", i.getbillamount())
        else:
            print(tourist_place)
    else:
        print(place_status)
    month = int(input("Enter the month: "))
    if month >= 1 and month <= 12:
        tourists_by_month = tr.searchtouristbymonth(month)
        if type(tourists_by_month) != str:
            for tourist_dict in tourists_by_month:
                print(f"touristid:{tourist_dict['touristid']} touristname:{tourist_dict['touristname']} place:{tourist_dict['place']} bookingdate:{tourist_dict['bookingdate']}")
        else:
            print(tourists_by_month)
    else:
        print("Invalid month")

if __name__ == "__main__":
    main()
