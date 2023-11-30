from binary_search import binarys_search

list = ["Sutton A&B", "Liverpool A&B", "Manchester A&B"]
search_term = input("enter hotel name:")
found = binarys_search(list,search_term)

if not found:
    print(f"{search_term} unknown entry")

if found:
    print(f"{search_term} appropriate entry ")