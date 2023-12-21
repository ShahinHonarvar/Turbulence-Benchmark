
def if_perfect_num(my_list):
    if my_list[28] == sum(filter(lambda x: x % my_list[28] == 0, range(1, my_list[28]))):
        return True
    else:
        return False
