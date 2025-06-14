
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate over the specified range of indices in my_list
    for i in range(10, 100):
        # If the current index has a positive integer value, add it to the pos_ints list
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 10 to index 100, both exclusive
    return pos_ints
