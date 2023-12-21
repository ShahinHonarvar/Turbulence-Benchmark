
def if_perfect_num(my_list):
    if my_list[17] == sum(filter(lambda x: x % my_list[17] == 0, my_list)):
        return True
    else:
        return False
