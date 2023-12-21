
def all_even_ints_inclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate through the list and append each even integer to the new list
    for i in range(80, 201):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
