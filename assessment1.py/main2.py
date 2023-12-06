from binary_search import binarys_search

Hotel_list = ["Sutton B&B", "Liverpool B&B", "Manchester B&B"]
breakfast_list = ["pancakes", "omelette", "french_toast" , "overnight_oats"]
bed_list = [1,2,3]
search_term_hotel = input("enter hotel name:")
search_term_breakfast = input("enter breakfast:")
search_term_bed = input("enter number of beds needed:")
found = binarys_search(Hotel_list,search_term_hotel,search_term_breakfast, search_term_bed)

if not found:
    print(f"{search_term_hotel}, {search_term_breakfast}, {search_term_bed} unknown entry")

if found:
    print(f"{search_term_hotel}, {search_term_breakfast}, {search_term_bed} appropriate entry")