from binary_search import hotel_search


hotel_type = ["liverpool", "manchester", "Sutton"]
Hotel_list = ["Sutton B&B", "Liverpool B&B", "Manchester B&B"]
breakfast_list = ["pancakes", "omelette", "french_toast","overnight_oats"]
bed_list = [1,2,3]
search_hotel_type = input("enter hotel type: e.g. Sutton, liverpool, manchester ")
search_term_hotel = input("enter hotel name: e.g. Sutton B&B, Liverpool B&B, Manchester B&B")
search_term_breakfast = input("enter breakfast:e.g. pancakes, omelette, french_toast , overnight_oats")
search_term_bed = input("enter number of beds needed:e.g. 1, 2 , 3 bedrooms")
found = hotel_search(Hotel_list,search_term_hotel,search_term_breakfast, search_term_bed, hotel_type)

if not found:
    print(f"{search_term_hotel}, {search_term_breakfast}, {search_term_bed}, {hotel_type} unknown entry")

if found:
    print(f"{search_term_hotel}, {search_term_breakfast}, {search_term_bed}, {hotel_type} appropriate entry")