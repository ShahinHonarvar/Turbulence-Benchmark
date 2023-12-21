
def sum_ints_div_by_either_nums(lst):
    return sum(x for x in lst if x % 1 == 0 or x % -1 == 0) if lst else 0
