
def if_perfect_num(my_list):
    return my_list[632] == sum(i for i in range(1, my_list[632]) if my_list[632] % i == 0)
