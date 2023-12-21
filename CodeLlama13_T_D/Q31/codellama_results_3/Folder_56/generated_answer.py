
def if_perfect_num(my_list):
    if len(my_list) > 60 and my_list[60] % sum(my_list[:60]) == 0:
        return True
    else:
        return False
