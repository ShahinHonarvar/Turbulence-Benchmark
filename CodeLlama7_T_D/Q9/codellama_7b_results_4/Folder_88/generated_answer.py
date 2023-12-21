
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the specified range of indices in the input list
    for i in range(4, 9):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the output list
            odd_ints.append(my_list[i])
    # Return the output list of all odd integers from index 4 to index 8, both inclusive
    return odd_ints
