class Hotel:
    def __init__(self,hotel,name, address,items ,filename):
        self.my_list = []
        self.hotel = hotel
        self.name = name
        self.address = address
        self.add_my_breakfast = []
        self.my_bedrooms = []
        self.items = []
        self.filename = filename
        self.hotels = self.load_hotels()


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


    def save_hotel(self):
        with open(self.filename, "w") as file:
            for hotel in self.hotels:
                file.write(f"{hotel['name']},{hotel['rating']},{hotel['price']}n")


    def load_hotels(self):
        hotels = []
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    name,rating,price = line.strip().split(',')
                    hotels.append({"name":name,"rating":float(rating), "price": float(price)})
        except FileNotFoundError:
            print("file not found. stating with an empty list of hotels")
        return hotels



    def select_hotel(self):
        print("Select a hotel ")
        for index, hotel in enumerate(self.hotels,start=1):
            print(f"f{index}. {hotel['name']} - Rating: {hotel['rating']} - Price:{hotel['price']}")
        while True:
            choice = input("Enter the number of the hotel you want to select:")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.hotels):
                    return self.hotels[choice - 1]
                print("Invalid choice. Please enter a valid number.")


    def user_enquiries(self):
        print("search for a hotel:")
        user_criteria = input("are the rooms available for any hotels,rating, or price:")





    def customer_information(self):
        self.name = input("enter your name: ")
        self.address = input("enter your address:")
        self.hotel = input("enter the hotel you want:")
        return self.name, self.address, self.hotel
    def route_function_hotel(self,hotel_name,destination):
        # Simulated directions
        directions = {
            'train station': 'take a right from the hotel, walk straight for 10 minutes, and you will find the train station.',
            'park': 'the nearest park is 5 minutes away from the hotel. Go left and walk until you see the park entrance.',
            'cafe': 'there is a cafe nearby. walk straight, and you will find it',
            'war memorial':'head straight. Then turn left from the main road. finally in 15 minutes  you will reach it.',
            'car park' : 'the car park will be opposite to the hotel. you can park your car there.'
        }
        if hotel_name.lower() == 'all' :
            for destination_name, directions in directions.items():
                if destination.lower() in destination_name:
                    print(f"Directions to {hotel_name} : {destination_name}")
                    break
        else:
            for destination_name, directions in directions.items():
                if destination.name.lower() == destination.lower():
                    print(f"directions from {hotel_name} to {destination_name}")
                    break
            else:
                print(f"destination '{destination}' not found.")