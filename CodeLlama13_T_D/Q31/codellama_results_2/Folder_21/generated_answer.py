
def if_perfect_num(my_list):
    if my_list[410] % sum(my_list[410-1:410+1]) == 0:
        return True
    else:
        return False
