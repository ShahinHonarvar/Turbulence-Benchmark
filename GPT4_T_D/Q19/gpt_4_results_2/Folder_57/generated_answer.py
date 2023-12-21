
def all_ints_not_div_by_num(lst):
    if len(lst) > 56 and len(lst) > 88:
        return [x for x in lst[57:88] if x % -59 != 0]
    else:
        return []
