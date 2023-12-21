
def sum_ints_div_by_either_nums(lst):
    return sum(x for x in lst[10:76] if x % -40 == 0 or x % -12 == 0)
