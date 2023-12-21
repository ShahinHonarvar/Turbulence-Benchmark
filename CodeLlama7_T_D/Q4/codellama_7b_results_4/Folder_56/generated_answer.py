
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Loop through the specified range of indices in my_list
    for i in range(7, 10):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
