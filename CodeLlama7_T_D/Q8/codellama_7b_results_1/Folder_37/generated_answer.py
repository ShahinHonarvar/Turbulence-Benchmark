
def all_even_ints_exclusive(my_list):
    # Create a new list to store the even integers
    even_ints = []
    # Iterate over the list of integers and append each even integer to the new list
    for i in range(1, len(my_list)):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
