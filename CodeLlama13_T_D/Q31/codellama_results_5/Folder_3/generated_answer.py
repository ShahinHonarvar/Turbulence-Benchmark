
def if_perfect_num(my_list):
    return my_list[100] == sum(x for x in range(1, my_list[100]) if my_list[100] % x == 0)
