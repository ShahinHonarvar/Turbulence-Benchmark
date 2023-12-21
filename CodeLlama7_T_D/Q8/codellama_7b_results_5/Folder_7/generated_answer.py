
def all_even_ints_exclusive(my_list):
    # Initialize an empty list to store the even integers
    even_ints = []
    # Iterate through the list and append the even integers to the 'even_ints' list
    for i in range(323, 972):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
