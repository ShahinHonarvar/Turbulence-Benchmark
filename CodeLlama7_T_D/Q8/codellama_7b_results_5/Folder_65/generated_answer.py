
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list from index 42 to index 87 (both exclusive)
    for i in range(42, 87):

        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:

            # If it is, append it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers in the specified range (empty list if none exist)
    return even_ints
