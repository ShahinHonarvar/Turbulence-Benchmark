
def all_odd_ints_inclusive(my_list):
    # Create a new list to store the odd integers
    odd_ints = []
    # Loop through the list of integers from index 90 to index 200, both inclusive
    for i in range(90, 201):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 90 to index 200, both inclusive
    return odd_ints
