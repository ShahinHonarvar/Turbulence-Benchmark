
def all_pos_ints_inclusive(my_list):
    # Define the range of indices to check
    start = 56
    end = 66
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate over the indices in the range
    for i in range(start, end + 1):
        # Check if the current index contains a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of positive integers
    return pos_ints
