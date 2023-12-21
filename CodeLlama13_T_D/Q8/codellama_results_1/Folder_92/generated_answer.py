
def all_even_ints_exclusive(my_list):
    even_ints = []
    for i in range(2, len(my_list), 2):
        even_ints.append(my_list[i])
    return even_ints
