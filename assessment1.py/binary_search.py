def hotel_search(list,search_term_hotel,search_term_breakfast,search_term_bed, hotel_type):
    start = 0
    end = len(list)-1

    found = False

    while found <= False and end >= start:
        midpoint = (start + end) // 2

        if list[midpoint] == hotel_search(search_term_hotel,search_term_breakfast,search_term_bed, hotel_type):
            found = True
        elif hotel_type < list[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return found