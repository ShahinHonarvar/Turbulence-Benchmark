
def all_pos_ints_exclusive(my_list):
    # Initialize an empty list to store the positive integers
    pos_ints = []

    # Iterate through the list of integers, starting at index 7 and ending before index 9 (inclusive)
    for i in range(7, len(my_list)):
        # If the current element is a positive integer, append it to the list of positive integers
        if my_list[i] > 0:
            pos_ints.append(my_list[i])

    # Return the list of all positive integers from index 7 to index 9 (exclusive), or an empty list if no positive integers exist in the specified range
    return pos_ints
