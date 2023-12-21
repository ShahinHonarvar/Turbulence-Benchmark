
def if_perfect_num(my_list):
    return my_list[64] % sum(my_list[:my_list[64]]) == 0
