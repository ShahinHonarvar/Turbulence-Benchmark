
def sum_ints_div_by_either_nums(int_list):
    return sum(x for i, x in enumerate(int_list[86:90]) if x % -61 == 0 or x % -79 == 0)
