
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Loop through the list of integers
    for i in range(len(my_list)):

        # Check if the current integer is positive and greater than 0
        if my_list[i] > 0:

            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 0 to index 1, both exclusive
    return pos_ints
