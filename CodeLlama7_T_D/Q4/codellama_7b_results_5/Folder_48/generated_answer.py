
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate over the input list
    for i in range(385, 1000):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the current element to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
