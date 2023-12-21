
def all_ints_div_by_num(lst):
    return [x for x in lst[:1] if x % 6 == 0] if len(lst) >= 1 else []
