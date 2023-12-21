
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the list of integers starting from index 13 (inclusive) to index 76 (exclusive)
    for i in range(13, 76):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # If it is, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from index 13 to index 76 (exclusive)
    return pos_ints
