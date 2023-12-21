
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the indices of the input list
    for i in range(385, 1000):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # If it does, add it to the output list
            odd_ints.append(my_list[i])
    # Return the output list of odd integers
    return odd_ints
