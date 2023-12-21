
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers starting from index 28 (inclusive) to index 49 (exclusive)
    for i in range(28, 49):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 28 to index 49 (exclusive)
    return pos_ints
