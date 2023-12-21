
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the specified range of indices in the input list
    for i in range(743, 867):
        # Check if the current index in the input list contains a positive integer
        if my_list[i] > 0:
            # If it does, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from the specified range, both exclusive
    return pos_ints
