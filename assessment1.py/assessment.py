
class Hotel:
    def __init__(self):
        self.my_list = ["Sutton B&B", "Liverpool B&B","Manchester B&B"]
        self.add_my_breakfast = ["pancakes","omelette","french_toast","overnight_oats"]
        self.my_bedrooms = [4,2,1,3]
        self.items = []
    def add_to_list(self,item):
        if not hasattr(self, "hotel_list"):
            self.my_list = []
        self.my_list.append(item)
        print(self.my_list)


    def add_my_breakfast(self,item):
        if not hasattr(self, "breakfast"):
            self.add_my_breakfast = []
        self.add_my_breakfast.append(item)
        print(self.add_my_breakfast)



    def add_my_bed(self,number):
        if not hasattr(self, "bedrooms"):
            self.my_bedrooms = []
        self.my_bedrooms.append(number)
        print(self.my_bedrooms)



    def is_empty(self):
        return len(self.items) == 0


    def push(self,item):
        self.items.append(item)


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "stack is empty"


    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "stack is empty"


    def size(self):
        return len(self.items)


    def customer_information(self):
        self.name = input("enter your name: ")
        self.address = input("enter your address:")
        self.hotel = input("enter the hotel you want:")
        print(f"\n customer_information:")
        print(f"f{self.hotel}")
        print(f"{self.name}")
        print(f"{self.address}")
        return self.hotel, self.name, self.address


customer = Hotel()

name,address, hotel = customer.customer_information()


item_to_add_list = input("Enter hotel in the hotel_list:")
customer.add_to_list(item_to_add_list)

add_my_bed = int(input("Enter number of bedroom:"))
customer.add_my_bed(add_my_bed)

add_my_breakfast = input("Enter breakfast option:")
