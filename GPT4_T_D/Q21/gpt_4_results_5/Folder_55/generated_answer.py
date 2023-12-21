
def all_ints_div_by_num(lst):
    if len(lst) < 2:
        return []
    return [x for x in lst[0:2] if x % 2 == 0]
