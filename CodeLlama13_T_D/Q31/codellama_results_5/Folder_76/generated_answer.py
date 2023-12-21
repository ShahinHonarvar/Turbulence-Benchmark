
def if_perfect_num(my_list):
    return my_list[537] == sum(filter(lambda x: x <= my_list[537] // 2, range(1, my_list[537])))
