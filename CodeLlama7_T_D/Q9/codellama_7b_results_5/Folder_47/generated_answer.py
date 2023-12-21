
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(37, 76 + 1):
        # If the current element is an odd integer, add it to the output list
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    # Return the output list of all odd integers from the specified range
    return odd_ints
