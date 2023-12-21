
def all_odd_ints_exclusive(my_list):
    # Get the range of indices for the specified range
    start_idx = 20
    end_idx = 35
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the range of indices
    for i in range(start_idx, end_idx):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from the specified range, exclusive
    return odd_ints
