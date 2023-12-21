
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    results = []

    # Loop through the list from index 60 to index 200, both exclusive
    for i in range(60, 200):
        # If the current element is a positive integer, add it to the results list
        if my_list[i] > 0:
            results.append(my_list[i])

    return results
