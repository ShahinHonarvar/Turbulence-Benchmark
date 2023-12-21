
def all_ints_div_by_num(lst):
    if len(lst) > 0:
        return [lst[0]] if lst[0] % 1 == 0 else []
    else:
        return []
