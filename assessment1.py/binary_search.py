import math
def binarys_search(list, search_term):
    start = 0
    end = len(list)-1

    found = False

    while found == False and end >= start:
        midpoint = math.floor((start + end) / 2)

        if list[midpoint] == search_term:
            found = True
        elif search_term < list[midpoint]:
            end = midpoint - 1
        else: start = midpoint + 1


    return found