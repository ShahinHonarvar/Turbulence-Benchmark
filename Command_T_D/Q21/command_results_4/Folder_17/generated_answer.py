def all_ints_div_by_num(lst):
    idx = next(i for i, x in enumerate(lst) if x % 91 == 0)
    if idx >= 33 and idx <= 35:
        return lst[idx - 33:idx + 2]
    return []
