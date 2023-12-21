
def if_perfect_num(my_list):
    return my_list[29] == sum(filter(lambda x: x % my_list[29] == 0, range(1, my_list[29])))
