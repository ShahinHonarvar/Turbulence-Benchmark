
def all_pos_ints_exclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(3, 8):
        # Check if the current element is a positive integer
        if isinstance(my_list[i], int) and my_list[i] > 0:
            # If it is, add it to the pos_ints list
            pos_ints.append(my_list[i])
    # Return the pos_ints list
    return pos_ints
