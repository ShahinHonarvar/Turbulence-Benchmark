
def if_perfect_num(my_list):
    return my_list[18] == sum(set(filter(lambda x: x < my_list[18], my_list)))
