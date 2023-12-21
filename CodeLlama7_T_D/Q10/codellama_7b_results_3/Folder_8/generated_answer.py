
def all_odd_ints_exclusive(my_list):
    # Check if the list is valid
    if not my_list:
        return []

    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Iterate over the list, starting from index 56
    for i in range(56, len(my_list)):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 56 to index 92, both exclusive
    return odd_ints
