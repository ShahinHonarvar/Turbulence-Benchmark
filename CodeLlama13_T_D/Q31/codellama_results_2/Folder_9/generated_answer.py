
def if_perfect_num(my_list):
    if my_list[24] == sum(my_list[:24]) + 1:
        return True
    else:
        return False
