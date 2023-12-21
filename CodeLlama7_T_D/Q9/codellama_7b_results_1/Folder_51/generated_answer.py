
def all_odd_ints_inclusive(my_list):
    # Create an empty list to store the odd integers
    odd_integers = []

    # Iterate through the list of integers
    for i in range(1, len(my_list) + 1):
        # Check if the current integer is odd
        if my_list[i] % 2 != 0:
            # Add the odd integer to the list
            odd_integers.append(my_list[i])

    # Return the list of all odd integers from index 1 to index 8, both inclusive
    return odd_integers
