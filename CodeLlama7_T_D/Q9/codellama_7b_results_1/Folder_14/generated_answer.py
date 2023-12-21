
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list of integers
    for i in range(5, 8):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # Add the odd integer to the new list
            odd_ints.append(my_list[i])
    # Return the list of all odd integers
    return odd_ints
