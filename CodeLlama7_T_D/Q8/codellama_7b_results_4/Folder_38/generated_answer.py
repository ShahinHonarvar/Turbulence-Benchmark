
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list from index 15 to index 40, both exclusive
    for i in range(15, 40):
        # If the current element is even, append it to the result list
        if my_list[i] % 2 == 0:
            result.append(my_list[i])

    # Return the result list

    return result
