
def sum_ints_div_by_either_nums(int_list):
    return sum(n for i, n in enumerate(int_list[10:77]) if n % -40 == 0 or n % -12 == 0)
