
def if_perfect_num(my_list):
    if my_list[23] == sum(filter(lambda x: x % my_list[23] == 0, range(1, my_list[23]))):
        return True
    else:
        return False
