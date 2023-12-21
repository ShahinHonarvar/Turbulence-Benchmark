
def all_even_ints_inclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and append even integers to the 'even_ints' list
    for i in range(90, 201):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    # Return the list of all even integers from index 90 to index 200, both inclusive
    return even_ints
