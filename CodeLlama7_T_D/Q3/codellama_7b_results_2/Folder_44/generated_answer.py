
def all_pos_ints_inclusive(my_list):
    # Find the starting and ending indices of the range
    start = 13
    end = 68
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the range of indices
    for i in range(start, end + 1):
        # Check if the current index contains a positive integer
        if my_list[i] > 0:
            # If it does, add it to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of all positive integers from the specified range
    return pos_ints
