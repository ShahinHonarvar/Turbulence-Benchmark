
def sum_ints_div_by_either_nums(my_list):
    return sum([x for x in my_list[154:798+1] if x % 275 == 0 or x % 580 == 0])
