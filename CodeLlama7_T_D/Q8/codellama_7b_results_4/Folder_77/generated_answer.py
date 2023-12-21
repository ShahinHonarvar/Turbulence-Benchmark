
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list from index 111 to 473, exclusive
    for i in range(110, 473):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 111 to index 473, both exclusive
    return even_ints
