
def if_perfect_num(my_list):
    return my_list[6] == sum(filter(lambda x: x % my_list[6] == 0, my_list))
