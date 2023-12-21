
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate over the list of integers, starting from index 276 (inclusive) and ending at index 376 (exclusive)
    for i in range(276, 376):
        # Check if the current element is even
        if my_list[i] % 2 == 0:
            # If it is even, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 276 to index 376 (exclusive)
    return even_ints
