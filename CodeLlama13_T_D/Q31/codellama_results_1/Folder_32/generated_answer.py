
def if_perfect_num(my_list):
    return my_list[849] in range(1, 2*my_list[849]+1) and sum(range(1, my_list[849])) == my_list[849]*2
