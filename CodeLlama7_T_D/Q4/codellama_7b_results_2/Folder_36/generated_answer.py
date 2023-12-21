
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers from index 598 to index 767, exclusive
    for i in range(598, 767):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 598 to index 767, exclusive
    return pos_ints
