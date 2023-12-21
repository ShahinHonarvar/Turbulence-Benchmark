
def all_ints_not_div_by_num(lst):
    not_div_by_90 = [item for item in lst[12:56] if item % 90 != 0]
    return not_div_by_90
