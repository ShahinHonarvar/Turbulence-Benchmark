
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of indices in my_list
    for i in range(len(my_list)):
        # Check if the current element is a positive integer
        if type(my_list[i]) == int and my_list[i] > 0:
            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
