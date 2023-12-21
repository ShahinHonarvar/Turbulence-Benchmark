
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[36:86]
    return sum(x for x in subset if x % -27 == 0 or x % -96 == 0)
