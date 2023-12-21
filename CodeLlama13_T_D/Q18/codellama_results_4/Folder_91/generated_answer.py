
def sum_ints_div_by_either_nums(my_list):
    return sum(x for x in my_list[0:5] if (x % 8 == 0 or x % -3 == 0))
