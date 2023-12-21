
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from index 1 to index 5, both inclusive
    for i in range(1, 6):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 1 to index 5, both inclusive
    return odd_ints
