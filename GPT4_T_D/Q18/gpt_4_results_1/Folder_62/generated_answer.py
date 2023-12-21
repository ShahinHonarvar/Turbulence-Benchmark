
def sum_ints_div_by_either_nums(lst):
    return sum(x for i, x in enumerate(lst[44:60]) if x % 15 == 0 or x % 39 == 0)
