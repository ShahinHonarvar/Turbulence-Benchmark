
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []

    # Iterate through the list and check if each element is even
    for i in range(22, 24):
        if my_list[i] % 2 == 0:
            # If the element is even, append it to the 'even_ints' list
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 22 to index 24, both exclusive
    return even_ints
