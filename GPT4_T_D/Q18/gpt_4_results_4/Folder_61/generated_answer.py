
def sum_ints_div_by_either_nums(int_list):
    return sum(n for i, n in enumerate(int_list[:7]) if n % -5 == 0 or n % -6 == 0)
