
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list of integers
    for i in range(28, 39):

        # Check if the current integer is even
        if my_list[i] % 2 == 0:

            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 28 to index 38, both inclusive
    return even_ints
