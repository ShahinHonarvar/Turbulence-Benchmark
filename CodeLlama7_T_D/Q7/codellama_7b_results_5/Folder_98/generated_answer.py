
def all_even_ints_inclusive(my_list):
    # Create an empty list to store the even integers
    even_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(len(my_list)):

        # Check if the current element is even
        if my_list[i] % 2 == 0:

            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 0 to index 6, both inclusive
    return even_ints
