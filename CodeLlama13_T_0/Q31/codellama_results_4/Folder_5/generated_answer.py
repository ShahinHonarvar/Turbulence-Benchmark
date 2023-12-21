
def if_perfect_num(my_list):
    if my_list[67] == sum(filter(lambda x: x % my_list[67] == 0, range(1, my_list[67]))):
        return True
    else:
        return False
