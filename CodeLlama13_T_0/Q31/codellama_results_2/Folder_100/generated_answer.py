
def if_perfect_num(my_list):
    if my_list[99] == sum(my_list[:my_list[99]]) and all(x < my_list[99] for x in my_list[:my_list[99]]):
        return True
    else:
        return False
