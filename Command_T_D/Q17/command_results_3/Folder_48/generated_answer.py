
def all_ints_div_by_both_two_nums(lst):
    lst = [e for e in lst if e % 982 == 0 and e % 319 == 0]
    return lst if len(lst) > 0 else []
