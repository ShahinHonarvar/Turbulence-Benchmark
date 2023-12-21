
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of the input list
    for i in range(22, 24):

        # Check if the current element is a positive integer
        if my_list[i] > 0:

            # If it is, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
