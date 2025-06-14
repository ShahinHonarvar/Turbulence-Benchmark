
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list of integers, starting from index 2 (the third element) and ending at index 5 (the sixth element), both exclusive
    for i in range(2, 6):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers in the specified range, or an empty list if no odd integers exist
    return odd_ints
