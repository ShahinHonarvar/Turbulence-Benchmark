
def sum_ints_div_by_either_nums(int_list):
    return sum(x for i, x in enumerate(int_list[3:10]) if x % 6 == 0 or x % 1 == 0)
