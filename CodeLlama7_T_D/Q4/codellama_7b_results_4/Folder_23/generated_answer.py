
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Loop through the specified range of indices in 'my_list'
    for i in range(29, 53):

        # Check if the current index contains a positive integer. If it does, add it to the 'pos_ints' list.
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the 'pos_ints' list containing all positive integers from index 29 to index 53, both exclusive. If no positive integers exist in the specified range, the function should return an empty list.
    return pos_ints
