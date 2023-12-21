
def if_perfect_num(my_list):
    return my_list[276] == sum(i for i in range(1, my_list[276]) if my_list[276] % i == 0)
