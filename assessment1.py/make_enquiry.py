class HotelEnquiry:
    def __init__(self,hotel_name, enquiry_qry ):
        self.hotel_name = hotel_name
        self.enquiry_qry = enquiry_qry



enquiries = []

def make_enquiry(hotel_name, enquiry_qry):
    new_enquiry = HotelEnquiry(hotel_name, enquiry_qry)
    enquiries.append(new_enquiry)
    enquiries.sort(key=lambda x: x.hotel_name)

def answer_inquiry():
    if enquiries:
        hotel_to_find = input("enter the desired breakfast to answer:")
        left, right = 0, len(enquiries) - 1
        while  left <= right:
            midpoint = (left + right) // 2
            if enquiries[midpoint].hotel_name == hotel_to_find:
                print(f"Enquiry for {enquiries[midpoint].hotel_name}: {enquiries[midpoint].enquiry_qry} - answered")
                enquiries.pop(midpoint)
                return
            elif enquiries[midpoint].hotel_name < hotel_to_find:
                left = midpoint + 1
            else:
                right = midpoint - 1
        print("yes we serve breakfast option such as pancakes, overnight_oat, omelette,")
        print("your option has been accept ")



make_enquiry("is hotel sutton B&B", "is there any rooms available?")
make_enquiry("is hotel Liverpool B&B", "is there any rooms available?")
answer_inquiry()
answer_inquiry()
