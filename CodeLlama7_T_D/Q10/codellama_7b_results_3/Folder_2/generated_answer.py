
def all_odd_ints_exclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Loop through the list of integers, starting from index 36 and ending at index 52 (both exclusive)
    for i in range(36, 52):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # If it is odd, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers in the specified range (both exclusive)
    return odd_ints
