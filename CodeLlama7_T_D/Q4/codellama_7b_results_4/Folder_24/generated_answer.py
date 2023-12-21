
def all_pos_ints_exclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []

    # Iterate over the specified range of indices in the input list
    for i in range(13, 66):

        # Check if the current index in the input list contains a positive integer
        if my_list[i] > 0:

            # Add the positive integer to the new list
            pos_ints.append(my_list[i])

    # Return the new list of positive integers, or an empty list if no positive integers exist in the specified range
    return pos_ints
