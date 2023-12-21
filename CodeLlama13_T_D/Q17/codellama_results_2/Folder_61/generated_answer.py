
def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst if (x % -5 == 0 and x % -6 == 0) and 0 <= x <= 6]
