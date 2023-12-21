
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate through the list of integers starting from index 20 (inclusive) to index 36 (exclusive)
    for i in range(20, 36):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the new list of even integers
            even_ints.append(my_list[i])
    # Return the new list of all even integers found in the specified range
    return even_ints
