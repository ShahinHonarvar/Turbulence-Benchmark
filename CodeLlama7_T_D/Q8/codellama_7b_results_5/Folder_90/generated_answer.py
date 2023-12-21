
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of indices in the list
    for i in range(389, 748):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If so, add it to the list of even integers
            even_ints.append(my_list[i])
    # Return the list of all even integers in the specified range, or an empty list if none exist
    return even_ints
