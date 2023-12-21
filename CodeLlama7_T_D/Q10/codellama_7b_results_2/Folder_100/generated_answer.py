
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the results
    odd_ints = []

    # Iterate through the list, starting from index 22 (inclusive) and ending at index 24 (exclusive)
    for i in range(22, 24):

        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:

            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 22 to index 24 (exclusive)
    return odd_ints
