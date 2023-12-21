
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the specified range of indices in my_list
    for i in range(90, 201):
        # Check if the current index in my_list is a positive integer
        if isinstance(my_list[i], int) and my_list[i] > 0:
            # If it is a positive integer, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers in the specified range, if any exist
    return pos_ints
