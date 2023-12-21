
def all_ints_not_div_by_num(lst):
    all_ints = lst[387:516]
    not_div_by_310 = [x for x in all_ints if x % 310 != 0]
    return not_div_by_310
