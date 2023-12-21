
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Loop through the list of integers, starting from index 18 (inclusive) and ending at index 60 (exclusive)
    for i in range(18, 60):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 18 to index 60, both exclusive
    return pos_ints
