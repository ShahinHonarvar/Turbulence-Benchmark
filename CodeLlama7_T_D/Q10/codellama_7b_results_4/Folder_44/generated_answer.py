
def all_odd_ints_exclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list, starting from index 81
    for i in range(81, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 81 to index 86, both exclusive
    return odd_ints
