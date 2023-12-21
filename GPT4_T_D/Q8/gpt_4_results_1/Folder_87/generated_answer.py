
def all_even_ints_exclusive(list_of_ints):
    even_list = []
    for i in range(33, 99):
        if list_of_ints[i] % 2 == 0:
            even_list.append(list_of_ints[i])
    return even_list
