
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list from index 2 to index 7, exclusive
    for i in range(2, 8):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the new list
            odd_ints.append(my_list[i])
    return odd_ints
