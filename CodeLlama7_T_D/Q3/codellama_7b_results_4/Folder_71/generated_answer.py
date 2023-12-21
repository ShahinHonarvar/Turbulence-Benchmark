
def all_pos_ints_inclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list from index 26 to index 52, both inclusive
    for i in range(26, 53):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers in the specified range
    return pos_ints
