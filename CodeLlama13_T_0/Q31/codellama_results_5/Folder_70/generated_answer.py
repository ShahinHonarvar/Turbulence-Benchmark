
def if_perfect_num(my_list):
    return my_list[845] == sum(filter(lambda x: x % my_list[845] == 0, range(1, my_list[845])))
