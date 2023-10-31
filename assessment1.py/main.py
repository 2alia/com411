from selection import selection_sort_hotels
#my hotel data is currently incorrect order
hotels_list = [
    {"name": "Sutton A&B", "ratings": 4.3, "price": 120 },
    {"name": "Liverpool A&B", "ratings": 4.1, "price": 100},
    {"name": "Manchester A&B", "ratings": 4.6, "price": 160},
]


#this used for to import function
selection_sort_hotels(hotels_list)
#print statement that comes at the beginning of the program
print("sorted hotels by name:")
#for loop that works for the hotel list
for hotel in hotels_list:
    print(hotel["name"],"-", hotel["ratings"], "-", hotel["price"])
#this prints all variables in the hotel list.