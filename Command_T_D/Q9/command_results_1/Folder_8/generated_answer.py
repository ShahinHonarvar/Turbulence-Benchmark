def all_odd_ints_inclusive(lst):
    if 23 in lst:
        odd_lst = [int(x) for x in lst[23:]]
        return odd_lst
    else:
        return []
