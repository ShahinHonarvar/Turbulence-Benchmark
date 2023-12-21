
def if_perfect_num(my_list):
    return my_list[985] == sum(x for x in range(1, int(my_list[985]) // 2 + 1) if my_list[985] % x == 0)
