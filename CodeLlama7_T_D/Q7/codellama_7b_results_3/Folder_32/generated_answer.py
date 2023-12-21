
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of indices
    for i in range(21, 97 + 1):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If so, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 21 to index 97, both inclusive
    return even_ints
