import math
def hotel_search(list, search_term_hotel,search_term_breakfast,search_term_bed,place_type ):
    start = 0
    end = len(list)-1

    found = False

    while found == False and end >= start:
        midpoint = math.floor((start + end) / 2)

        if list[midpoint] == search_term_hotel:
            found = True
        elif search_term_hotel < list[midpoint]:
            end = midpoint - 1
        else: start = midpoint + 1
        if list[midpoint] == search_term_breakfast:
            found = True
        elif search_term_breakfast < list[midpoint]:
            end = midpoint - 1
        else: start = midpoint + 1
        if list[midpoint] == search_term_bed:
            found = True
        elif search_term_bed < list[midpoint]:
            end = midpoint - 1
        else: start = midpoint + 1
        if list[midpoint] == place_type:
            found = True
        elif place_type < list[midpoint]:
            end = midpoint - 1
        else: start = midpoint + 1



    return found