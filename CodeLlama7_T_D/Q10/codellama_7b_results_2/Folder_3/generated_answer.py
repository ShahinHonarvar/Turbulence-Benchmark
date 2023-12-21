
def all_odd_ints_exclusive(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list from index 78 to index 93, both exclusive
    for i in range(78, 94):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 78 to index 93, both exclusive
    return odd_ints
