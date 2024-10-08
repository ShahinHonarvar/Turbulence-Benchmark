
def all_odd_ints_exclusive(my_list):
    # Create an empty list to store the result
    result = []

    # Iterate over the elements of the input list
    for i in range(56, 88):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
