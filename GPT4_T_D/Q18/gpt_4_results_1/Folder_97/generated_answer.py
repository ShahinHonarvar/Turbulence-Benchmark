
def sum_ints_div_by_either_nums(lst):
    return sum(x for i, x in enumerate(lst[58:76]) if x % 72 == 0 or x % 62 == 0)
