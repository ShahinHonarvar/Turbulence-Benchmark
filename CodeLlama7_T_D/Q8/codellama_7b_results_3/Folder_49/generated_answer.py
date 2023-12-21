
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate over the specified range of indices
    for i in range(80, 200):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If it does, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from the specified range, or an empty list if none exist
    return even_ints
