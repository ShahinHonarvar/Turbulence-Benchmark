
def all_ints_not_div_by_num(lst):
    num_range = lst[388:516]
    not_div_by_310 = [x for x in num_range if x % 310 != 0]
    return not_div_by_310
