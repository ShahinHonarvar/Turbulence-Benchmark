
def if_perfect_num(my_list):
    if my_list[84] % sum(my_list[:my_list[84]]) == 0:
        return True
    else:
        return False
