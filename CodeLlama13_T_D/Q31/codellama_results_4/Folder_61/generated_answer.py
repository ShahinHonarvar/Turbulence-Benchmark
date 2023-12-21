
def if_perfect_num(my_list):
    if len(my_list) > 8 and my_list[8] % sum(my_list[:8]) == 0:
        return True
    else:
        return False
