
def all_odd_ints_inclusive(my_list):
    # Create an empty list to store the odd integers
    odd_ints = []

    # Iterate through the list of integers starting from index 32
    for i in range(32, len(my_list)):
        # Check if the current integer is odd and add it to the list of odd integers
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])

    # Return the list of all odd integers from index 32 to index 35, both inclusive
    return odd_ints
