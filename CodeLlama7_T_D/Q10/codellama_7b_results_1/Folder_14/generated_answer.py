
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list of integers
    for i in range(1, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the new list
            odd_ints.append(my_list[i])
    # Return the new list of odd integers
    return odd_ints
