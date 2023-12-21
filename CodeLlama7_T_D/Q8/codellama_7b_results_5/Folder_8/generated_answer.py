
def all_even_ints_exclusive(my_list):
    start_index = 56
    end_index = 92
    even_ints = []
    for i in range(start_index, end_index):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
