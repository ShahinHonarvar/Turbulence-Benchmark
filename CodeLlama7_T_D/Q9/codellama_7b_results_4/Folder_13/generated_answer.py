
def all_odd_ints_inclusive(my_list):
    # Define the range of indices to check for odd integers
    start_idx = 25
    end_idx = 87
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the indices in the specified range
    for i in range(start_idx, end_idx + 1):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # If it does, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers found in the specified range
    return odd_ints
