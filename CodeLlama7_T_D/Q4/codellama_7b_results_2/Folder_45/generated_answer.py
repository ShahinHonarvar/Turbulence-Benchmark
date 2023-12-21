
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers, starting from index 30
    for i in range(30, len(my_list)):
        # Check if the current integer is positive and not equal to zero
        if my_list[i] > 0 and my_list[i] != 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 30 to index 200, both exclusive
    return pos_ints
