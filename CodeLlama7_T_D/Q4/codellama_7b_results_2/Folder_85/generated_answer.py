
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the specified range of indices in my_list
    for i in range(4, 6):
        # If the current index contains a positive integer, add it to the pos_ints list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    # Return the pos_ints list
    return pos_ints
