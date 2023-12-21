
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list from index 28 to index 53, exclusive
    for i in range(28, 53):

        # If the current element is even, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the 'even_ints' list
    return even_ints
