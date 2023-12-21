
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list of integers starting from index 28 (inclusive) and ending at index 49 (exclusive)
    for i in range(28, 49):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 28 to index 49, both exclusive
    return even_ints
