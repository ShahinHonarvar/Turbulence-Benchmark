
def all_odd_ints_exclusive(my_list):
    # Create an empty list to store the odd integers
    odd_ints = []

    # Iterate over the list of integers
    for i in range(len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list
            odd_ints.append(my_list[i])

    # Return the list of all odd integers in the specified range
    return odd_ints
