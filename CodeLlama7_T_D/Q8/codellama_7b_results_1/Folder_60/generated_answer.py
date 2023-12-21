
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the list of integers starting from index 44 (inclusive) and ending at index 91 (exclusive)
    for i in range(44, 91):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 44 to index 91 (exclusive)
    return even_ints
