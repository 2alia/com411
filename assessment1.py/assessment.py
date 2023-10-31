class Hotel:
    def __init__(self,hotels,name, address,items):
        self.my_list = []
        self.hotels = hotels
        self.name = name
        self.address = address
        self.add_my_breakfast = []
        self.my_bedrooms = []
        self.items = []


    def add_to_list(self):
        self.my_list = ["Sutton A&B", "Liverpool A&B"]
        self.my_list.append("Manchester A&B")
        print(self.my_list)


    def add_my_breakfast(self):
        self.add_my_breakfast = ["pancakes","omelette","french_toast"]
        self.add_my_breakfast.append("overnight_oats")
        print(self.add_my_breakfast)


    def add_my_bed(self):
        self.my_bedrooms = [4,2,1,3]
        self.my_bedrooms.append(5)
        print(self.my_bedrooms)


    def is_empty(self):
        return len(self.items) ==0


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
        self.hotels = input("enter the hotel you want:")
        return self.name, self.address, self.hotels
