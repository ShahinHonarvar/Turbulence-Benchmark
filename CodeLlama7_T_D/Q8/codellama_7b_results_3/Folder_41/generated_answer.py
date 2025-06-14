
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate over the list of integers
    for i in range(8, 10):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 8 to index 9, both exclusive
    return even_ints
