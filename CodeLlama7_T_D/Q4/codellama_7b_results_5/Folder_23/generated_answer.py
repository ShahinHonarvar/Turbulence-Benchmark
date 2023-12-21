
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the specified range of indices in my_list
    for i in range(29, 53):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the pos_ints list
            pos_ints.append(my_list[i])

    # Return the pos_ints list
    return pos_ints
