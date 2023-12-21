
def if_perfect_num(my_list):
    return my_list[64] in list(range(1, int(my_list[64])**0.5 + 1)) and sum(list(range(1, int(my_list[64])**0.5 + 1))) == my_list[64]
