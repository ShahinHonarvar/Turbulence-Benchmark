
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []

    # Loop through the list and append the even integers to the new list
    for i in range(22, 51):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])

    # Return the new list of all even integers from index 22 to index 50, both inclusive
    return even_ints
