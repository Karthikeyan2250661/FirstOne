# main.py
import tourist_service as ts
import utility as ut

def parse_tourist_input(input_data):
    # Try colon-separated first
    parts = input_data.split(':')
    if len(parts) == 5:
        name, place, date_str, days_str, tickets_str = parts
        # Normalize date to ddmmyyyy
        bookingdate = date_str.replace('/', '')
        try:
            noofdays = int(days_str)
            nooftickets = int(tickets_str)
        except ValueError:
            return None, None, None, None, None
        return name, place, bookingdate, noofdays, nooftickets

    # Fallback: concatenated format (touristname+place+ddmmyyyy+days+tickets)
    valid_places = ["Beach","Pilgrimage","Heritage","Hill Station","Water Falls","Adventures"]
    place = next((p for p in valid_places if p in input_data), None)
    if not place:
        return None, None, None, None, None
    i = input_data.find(place)
    name = input_data[:i]
    tail = input_data[i+len(place):]
    digits = ''.join(c for c in tail if c.isdigit())
    if len(digits) < 10:
        return None, None, None, None, None
    bookingdate = digits[:8]
    rest = digits[8:]
    # split rest into days/tickets
    if len(rest) == 2:
        d, t = rest
    elif len(rest) == 3:
        # try X,YZ first
        d, t = rest[0], rest[1:]
    else:
        d, t = rest[:-1], rest[-1]
    return name, place, bookingdate, int(d), int(t)

def main():
    tr = ts.Tourism()
    n = int(input("Enter the number of registrations: "))
    for idx in range(1, n+1):
        print(f"Enter the registration details {idx}")
        entry = input().strip()
        name, place, bd, days, tickets = parse_tourist_input(entry)
        if not name:
            print("Invalid input format")
            continue
        # Validate
        vp = ut.validateplace(place)
        if vp is not True:
            print(vp); continue
        vd = ut.validatedate(bd)
        if vd is not True:
            print(vd); continue
        # Generate ID and add
        tid = tr.generateid(name, bd)
        tr.addtouristdetails(tid, name, place, bd, days, tickets)

    # Retrieve by place
    place = input("Enter the Place to be searched: ").strip()
    vp = ut.validateplace(place)
    if vp is True:
        res = tr.retrievedetailsbyplace(place)
        if isinstance(res, str):
            print(res)
        else:
            for t in res:
                print("Tourist ID:", t.gettouristid())
                print("Tourist Name:", t.gettouristname())
                print("Number Of Days:", t.getnoofdays())
                print("Number Of Tickets:", t.getnooftickets())
                print("Bill Amount:", t.getbillamount())
    else:
        print(vp)

    # Retrieve by month
    m = int(input("Enter the month: "))
    if 1 <= m <= 12:
        res = tr.searchtouristbymonth(m)
        if isinstance(res, str):
            print(res)
        else:
            for d in res:
                print(f"tourist_id:{d['touristid']}\n tourist_name:{d['touristname']} place:{d['place']} bookingdate:{d['bookingdate']}")
    else:
        print("Invalid month")

if __name__ == "__main__":
    main()
