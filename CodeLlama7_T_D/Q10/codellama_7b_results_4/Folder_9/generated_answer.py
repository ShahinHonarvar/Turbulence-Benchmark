
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list of integers
    for i in range(70, 72):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers in the specified range
    return odd_ints
