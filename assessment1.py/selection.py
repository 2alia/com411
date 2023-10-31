def selection_sort_hotels(hotels):
    n =len(hotels)
    for i in range(n):
        lowest_index_so_far = i
        for j in range(i + 1, n):
            if hotels[j]["name"] < hotels[lowest_index_so_far]["name"]:
                lowest_index_so_far = j
        hotels[i], hotels[lowest_index_so_far] = hotels[lowest_index_so_far], hotels[i]