
def all_even_ints_exclusive(my_list):
    # Define a range of indices for the even integers
    range_indices = range(44, 67)
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the range of indices and check if each index value is even
    for i in range_indices:
        if my_list[i] % 2 == 0:
            # If the index value is even, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 44 to index 67, both exclusive
    return even_ints
