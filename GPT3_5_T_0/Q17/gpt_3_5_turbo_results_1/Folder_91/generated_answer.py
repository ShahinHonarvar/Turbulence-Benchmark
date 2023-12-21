
def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst[:5] if x % 8 == 0 and x % -3 == 0]
