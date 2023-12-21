
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Loop through the list and append each even integer to the 'even_ints' list
    for i in range(64, 80):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the 'even_ints' list
    return even_ints
