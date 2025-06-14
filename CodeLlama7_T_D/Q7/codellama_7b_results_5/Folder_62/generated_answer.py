
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Loop through the specified range of indices
    for i in range(91, 100):
        # Check if the current index contains an even integer
        if my_list[i] % 2 == 0:
            # If it does, add it to the list of even integers
            even_ints.append(my_list[i])
    return even_ints
