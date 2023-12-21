
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Iterate over the list of integers
    for i in range(2, 9):
        # Check if the current index contains an odd integer
        if my_list[i] % 2 != 0:
            # If it does, add it to the new list
            odd_ints.append(my_list[i])
    # Return the new list of odd integers
    return odd_ints
