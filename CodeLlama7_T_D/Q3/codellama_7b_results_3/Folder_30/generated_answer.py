
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the specified range of indices in my_list
    for i in range(55, 98 + 1):
        # Check if the current element is a positive integer
        if isinstance(my_list[i], int) and my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 55 to index 98, both inclusive
    return pos_ints
