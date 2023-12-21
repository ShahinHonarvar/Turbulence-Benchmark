
def if_perfect_num(my_list):
    if my_list[100] == sum(my_list[:my_list[100]]) and all(x < my_list[100] for x in my_list[:100]):
        return True
    else:
        return False
