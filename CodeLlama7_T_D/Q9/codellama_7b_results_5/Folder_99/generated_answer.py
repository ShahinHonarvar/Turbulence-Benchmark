
def all_odd_ints_inclusive(my_list):
    # Find the start and end indices of the range
    start = 310
    end = 370
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate over the specified range
    for i in range(start, end + 1):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from the specified range, or an empty list if no odd integers exist
    return odd_ints
