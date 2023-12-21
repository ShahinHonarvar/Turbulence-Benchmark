
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the specified range of the input list
    for i in range(5, 8):
        # If the current element is an even integer, append it to the output list
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    return even_ints
