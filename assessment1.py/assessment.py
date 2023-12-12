import json
from selection import selection_sort_hotels
class Hotel:
    def __init__(self):
        self.my_list = [] #Sutton B&B", "Liverpool B&B","Manchester B&B
        self.my_bedrooms = [] #self.my_bedrooms = [4,2,1,3]
        self.items = []
        self.Break = [] #pancakes","omelette","french_toast","overnight_oats
        self.name = []
        self.address = []
        self.type = []



    # my hotel data is currently incorrect order
    hotels_list = [
        {"name": "Sutton B&B", "ratings": 4.3, "price": 120},
        {"name": "Liverpool B&B", "ratings": 4.1, "price": 100},
        {"name": "Manchester B&B", "ratings": 4.6, "price": 160},
    ]

    # this used for to import function
    selection_sort_hotels(hotels_list)
    # print statement that comes at the beginning of the program
    print("sorted hotels by name:")
    # for loop that works for the hotel list
    for hotel in hotels_list:
        print(hotel["name"], "-", hotel["ratings"], "-", hotel["price"])

    # this prints all variables in the hotel list.
    def make_enquiry(self):
        print("welcome to our hotel enquiry system!")
        enquiry_type = input("what type of enquiry do you have? (e.g.rooms, events, breakfast)")
        if enquiry_type.lower() == "rooms":
            print("our hotel offers for bedrooms there is four bedrooms possible for purchase.")
        elif enquiry_type.lower() == "events":
            print("events are not currently on at the moment but will be shortly on the data 29th December")
        elif enquiry_type.lower() == "breakfast":
            print("breakfast option are pancakes,omelette,french_toast,overnight_oats")
        else:
            print("we didn't understand your enquiry ")
    def save_to_json(self, filename):
        data = {
            "customer_name": self.name,
            "customer_address": self.address,
            "customer_type": self.type,
            "hotel_list": self.my_list,
            "breakfast_option": self.Break,
            "bedroom_number": self.my_bedrooms
        }

        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Data saved to {filename} successfully!")

    def customer_type(self, type):
        self.type.append(type)
        print(self.type)

    def add_to_list(self, item):
        self.my_list.append(item)
        print(self.my_list)

    def customer_name(self,name):
        self.name.append(name)
        print(self.name)

    def customer_address(self, address):
        self.address.append(address)
        print(self.address)

    def append_to_break(self, item):
        self.Break.append(item)
        print(self.Break)
    def add_my_bed(self,number):
        self.my_bedrooms = []
        self.my_bedrooms.append(number)
        print(self.my_bedrooms)
    def display(self):
        print("\ncurrent Data:")
        print(f"name: {self.name}")
        print(f"address: {self.address}")
        print(f"type: {self.type}")
        print(f"hotel list: {self.my_list}")
        print(f"breakfast options: {self.Break}")
        print(f"bedroom Numbers: {self.my_bedrooms}")
    def customer_information(self):
        name = input("enter your name: ")
        address = input("enter your address:")
        customer_type = input("enter the type you want: e.g. Sutton, Liverpool , Manchester")
        self.customer_name(name)
        self.customer_address(address)
        self.customer_type(customer_type)
        return customer_type, name, address

customer = Hotel()
customer.save_to_json("hotel_data.json")
customer_type, name, address = customer.customer_information()

item_to_add_list = input("Enter hotel in the hotel_list:")
customer.add_to_list(item_to_add_list)

add_my_bed = int(input("Enter number of bedroom:"))
customer.add_my_bed(add_my_bed)

append_to_breakfast = input("Enter breakfast option:")
customer.append_to_break(append_to_breakfast)

customer.display()
customer.save_to_json("updated_hotel_data.json")
customer.make_enquiry()
