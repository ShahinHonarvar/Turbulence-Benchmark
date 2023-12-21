import bisect
def composite_nums_between_indices(lst):
    lst = lst[:]
    c = bisect.bisect_left(lst, 639)
    while c < len(lst) and lst[c] <= 975:
        c += 1
    return set(lst[c-1:c])
