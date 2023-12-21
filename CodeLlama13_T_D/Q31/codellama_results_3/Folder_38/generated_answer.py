
def if_perfect_num(my_list):
    if my_list[38] == sum(filter(lambda x: x % my_list[38] == 0, range(1, my_list[38]))) and all(map(lambda x: x < my_list[38], my_list)):
        return True
    else:
        return False
