
def if_perfect_num(my_list):
    if my_list[4] == sum(my_list[:4]) and all(x**2 for x in my_list[:4]):
        return True
    else:
        return False
