
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the list from index 66 to index 90, exclusive
    for i in range(66, 91):
        # If the current element is an odd integer, add it to the result list
        if my_list[i] % 2 != 0:
            result.append(my_list[i])

    # Return the result list
    return result
