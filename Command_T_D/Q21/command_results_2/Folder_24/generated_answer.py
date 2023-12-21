def all_ints_div_by_num(lst):
    return [x for x in range(12, 77 + 1) if x % -19 == 0 and x in lst]
