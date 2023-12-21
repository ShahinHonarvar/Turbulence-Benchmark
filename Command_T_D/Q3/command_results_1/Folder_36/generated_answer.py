def all_pos_ints_inclusive(lst):
    if not lst:
        return []
    if len(lst) < 247:
        return []
    return lst[246:750]
