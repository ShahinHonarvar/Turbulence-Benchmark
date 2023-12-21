
def all_pos_ints_exclusive(my_list):
    # Get the starting and ending indices of the range
    start_idx = 41
    end_idx = 69
    # Initialize an empty list to store the positive integers
    pos_ints = []
    # Iterate through the specified range of the input list
    for i in range(start_idx, end_idx):
        # Check if the current element is a positive integer
        if my_list[i] > 0:
            # Add the positive integer to the list of positive integers
            pos_ints.append(my_list[i])
    # Return the list of positive integers
    return pos_ints
