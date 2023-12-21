def all_ints_not_div_by_num(lst):
    if not lst:
        return []
    idx = next(i for i, x in enumerate(lst) if x % -514)
    return lst[:idx] + lst[idx + 1:]
