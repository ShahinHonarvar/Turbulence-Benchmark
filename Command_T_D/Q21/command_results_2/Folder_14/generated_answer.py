import bisect
def all_ints_div_by_num(lst):
    idx = bisect.bisect_left(lst, 8)
    if idx >= len(lst) - 1:
        return []
    x = lst[idx]
    idx += 1
    idx = bisect.bisect_left(lst, x+8)
    return lst[idx-1:idx+2]
