
def all_pos_ints_exclusive(my_list):
    # Create a new list to store the positive integers
    pos_ints = []

    # Loop through each integer in the input list
    for i in range(len(my_list)):

        # Check if the current integer is positive and not 0
        if my_list[i] > 0 and my_list[i] != 0:

            # Add the positive integer to the new list
            pos_ints.append(my_list[i])

    # Return the new list of all positive integers from index 0 to index 2, both exclusive
    return pos_ints
