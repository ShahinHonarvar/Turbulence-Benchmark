
def if_perfect_num(my_list):
    if len(my_list) > 88:
        return my_list[88] % sum(my_list[:88]) == 0
    else:
        return False
