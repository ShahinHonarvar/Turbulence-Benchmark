
def if_perfect_num(my_list):
    if my_list[63] == sum(my_list[:63]):
        return True
    else:
        return False
