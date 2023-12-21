
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers starting from index 28 and ending at index 40
    for i in range(28, 41):
        # Check if the current integer is positive
        if my_list[i] > 0:
            # If it is positive, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers in the specified range
    return pos_ints
