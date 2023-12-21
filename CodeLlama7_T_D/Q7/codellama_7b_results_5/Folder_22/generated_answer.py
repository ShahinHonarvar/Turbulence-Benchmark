
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(40, 201, 2):

        # If the current index contains an even integer, append it to the 'even_ints' list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 40 to index 200, both inclusive
    return even_ints
