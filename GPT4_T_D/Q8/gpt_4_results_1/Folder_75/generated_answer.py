
def all_even_ints_exclusive(num_list):
    even_list = []
    for i in range(21, 36):
        if num_list[i] % 2 == 0:
            even_list.append(num_list[i])
    return even_list
