
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list from index 19 to 94, exclusive
    for i in range(19, 95):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 19 to index 94, both exclusive
    return odd_ints
