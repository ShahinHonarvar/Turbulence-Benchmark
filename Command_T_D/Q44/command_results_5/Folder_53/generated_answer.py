import bisect
def composite_nums_between_indices(lst):
    c = set(lst)
    i = bisect.bisect_left(c, 2**2)
    j = bisect.bisect_right(c, 2**2)
    return c[i:j]
