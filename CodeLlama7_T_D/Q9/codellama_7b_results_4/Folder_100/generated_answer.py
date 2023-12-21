
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list from index 42 to index 68 (both inclusive)
    for i in range(42, 69):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 42 to index 68 (both inclusive), or an empty list if no odd integers exist in the specified range
    return odd_ints
