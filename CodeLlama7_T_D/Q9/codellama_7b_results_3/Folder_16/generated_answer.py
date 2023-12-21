 def all_odd_ints_inclusive(my_list):
    # Initialize a new empty list to store the odd integers
    odd_ints = []
    # Iterate over the specified range of indices in the input list
    for i in range(33, 37):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, append it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 33 to index 36, both inclusive
    return odd_ints
