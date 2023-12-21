
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(310, 371):
        # Check if the current index contains a positive integer
        if my_list[i] > 0:
            # If it does, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers found in the specified range of indices
    return pos_ints
