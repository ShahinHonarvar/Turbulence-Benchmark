
def all_even_ints_exclusive(int_list):
    even_list = []
    for i in range(599, 767):
        if int_list[i] % 2 == 0:
            even_list.append(int_list[i])
    return even_list
