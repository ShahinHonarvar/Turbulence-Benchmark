
def all_ints_not_div_by_num(my_list):
    return [x for x in my_list if x % 1 != 0 and x >= 0 and x < len(my_list)]
