
def all_odd_ints_inclusive(my_list):
    # Define a new list to store the odd integers
    odd_ints = []
    # Loop through the specified range of indices in the input list
    for i in range(55, 98 + 1):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the output list
            odd_ints.append(my_list[i])
    # Return the output list of odd integers
    return odd_ints
