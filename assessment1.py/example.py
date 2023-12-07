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
                name, rating, price = line.strip().split(',')
                hotels.append({"name": name, "rating": float(rating), "price": float(price)})
    except FileNotFoundError:
        print("file not found. stating with an empty list of hotels")
    return hotels


def select_hotel(self):
    print("Select a hotel ")
    for index, hotel in enumerate(self.hotels, start=1):
        print(f"f{index}. {hotel['name']} - Rating: {hotel['rating']} - Price:{hotel['price']}")
    while True:
        choice = input("Enter the number of the hotel you want to select:")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(self.hotels):
                return self.hotels[choice - 1]
            print("Invalid choice. Please enter a valid number.")