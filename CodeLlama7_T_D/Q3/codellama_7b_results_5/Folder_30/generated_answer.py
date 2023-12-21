
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(55, 98 + 1):
        # If the current element is a positive integer, add it to the output list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the output list of all positive integers in the specified range, or an empty list if no positive integers exist
    return pos_ints
