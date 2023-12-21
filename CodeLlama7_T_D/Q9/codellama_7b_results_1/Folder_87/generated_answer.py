
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []

    # Loop through the list from index 36 to 46, both inclusive
    for i in range(36, 47):
        # Check if the current element is odd
        if my_list[i] % 2 != 0:
            # Add the current element to the list of odd integers
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 36 to index 46, both inclusive
    return odd_ints
