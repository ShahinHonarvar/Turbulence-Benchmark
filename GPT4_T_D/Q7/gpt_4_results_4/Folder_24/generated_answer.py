
def all_even_ints_inclusive(int_list):
    even_list = []
    for i in range(74, 96):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_list.append(int_list[i])
    return even_list
