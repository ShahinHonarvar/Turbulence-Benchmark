
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(26, 53):

        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:

            # If it does, add it to the output list
            even_ints.append(my_list[i])

    # Return the output list of even integers
    return even_ints
