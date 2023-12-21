
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []

    # Iterate through the list of integers
    for i in range(29, 80):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the new list
            odd_ints.append(my_list[i])

    # Return the new list of odd integers
    return odd_ints
