
def all_ints_div_by_both_two_nums(lst):
    return [x for x in range(58, 81 + 1) if x % 55 == 0 and x % 10 == 0 and x in lst]
