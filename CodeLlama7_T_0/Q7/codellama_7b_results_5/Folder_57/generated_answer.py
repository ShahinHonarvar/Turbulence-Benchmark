
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and append the even integers to the 'even_ints' list
    for i in range(27, 56):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the 'even_ints' list
    return even_ints
