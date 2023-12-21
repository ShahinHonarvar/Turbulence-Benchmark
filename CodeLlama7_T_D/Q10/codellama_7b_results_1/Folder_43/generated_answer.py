 def all_odd_ints_exclusive(my_list):
    # Initialize a new list to store the odd integers
    odd_ints = []
    # Loop through the elements of the input list
    for i in range(38, 77):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # If it is, add it to the list of odd integers
            odd_ints.append(my_list[i])
    # Return the list of all odd integers from index 38 to index 77, both exclusive
    return odd_ints
