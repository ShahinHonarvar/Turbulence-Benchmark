
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate over the list of integers, starting from index 13 (inclusive) and ending at index 66 (exclusive)
    for i in range(13, 66):
        # Check if the current element is an even integer
        if my_list[i] % 2 == 0:
            # If it is, add it to the list of even integers
            even_ints.append(my_list[i])
    return even_ints
