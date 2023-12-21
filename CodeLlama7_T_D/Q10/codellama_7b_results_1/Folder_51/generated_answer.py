
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Loop through the specified range of the input list
    for i in range(6, 10):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the new list
            odd_ints.append(my_list[i])

    # Return the new list of all odd integers found in the specified range
    return odd_ints
