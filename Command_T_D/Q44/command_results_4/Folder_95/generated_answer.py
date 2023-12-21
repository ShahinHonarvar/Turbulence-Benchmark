import bisect
def composite_nums_between_indices(lst):
    idx26 = bisect.bisect_left(lst, 26)
    idx52 = bisect.bisect_left(lst, 52)
    return set(lst[idx26:idx52])
