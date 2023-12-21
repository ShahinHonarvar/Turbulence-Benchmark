
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate over the specified range of indices in the input list
    for i in range(64, 80):
        # If the current index contains an even integer, append it to the output list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
