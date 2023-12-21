
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Iterate over the specified range of the input list
    for i in range(32, 100):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the output list
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 32 to index 99, both exclusive
    return odd_ints
