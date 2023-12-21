
def all_odd_ints_inclusive(my_list):
    # Initialize an empty list to store the odd integers
    odd_ints = []
    # Iterate through the list starting from index 34 to 55 (both inclusive)
    for i in range(34, 56):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 34 to index 55 (both inclusive), or an empty list if no odd integers exist in the specified range.
    return odd_ints
