
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and check if each element is even
    for i in range(295, 573):
        if my_list[i] % 2 == 0:
            # If the element is even, add it to the 'even_ints' list
            even_ints.append(my_list[i])

    # Return the 'even_ints' list
    return even_ints
