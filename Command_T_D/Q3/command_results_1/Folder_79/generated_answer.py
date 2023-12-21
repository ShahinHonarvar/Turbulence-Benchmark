def all_pos_ints_inclusive(lst):
    res = []
    lst_len = len(lst)
    if lst_len > 4:
        res += lst[4:lst_len]
    return res
