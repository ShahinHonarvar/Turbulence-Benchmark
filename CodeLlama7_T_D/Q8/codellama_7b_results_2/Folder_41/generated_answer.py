
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Iterate through the list and append the even integers to the new list
    for i in range(8, 10):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the list of all even integers from index 8 to index 9, both exclusive
    return even_ints
