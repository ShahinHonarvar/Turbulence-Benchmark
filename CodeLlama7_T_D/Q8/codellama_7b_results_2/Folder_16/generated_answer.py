
def all_even_ints_exclusive(my_list):
    # Define the range of even integers
    even_ints = []
    for i in range(86, 90):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
