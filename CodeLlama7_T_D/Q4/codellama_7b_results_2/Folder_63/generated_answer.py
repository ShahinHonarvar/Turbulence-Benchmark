
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the list of integers
    for i in range(38, 52):
        # Check if the current integer is positive
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers in the specified range, both exclusive
    return pos_ints
