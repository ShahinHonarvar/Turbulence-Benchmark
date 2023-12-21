 def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Loop through the specified range of the input list
    for i in range(36, 85):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the new list
            even_ints.append(my_list[i])
    # Return the new list of even integers
    return even_ints
