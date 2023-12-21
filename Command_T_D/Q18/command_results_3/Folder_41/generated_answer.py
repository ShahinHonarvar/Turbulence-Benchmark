
def sum_ints_div_by_either_nums(lst):
    return sum(n for n in lst if n % 6 == 0 or n % 6 == -3)
