
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Loop through the list of integers starting from index 43 (inclusive) and ending at index 99 (exclusive)
    for i in range(43, 100):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is a positive integer, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers in the specified range
    return pos_ints
