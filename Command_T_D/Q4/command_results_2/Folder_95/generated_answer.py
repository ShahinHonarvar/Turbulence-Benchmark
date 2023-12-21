def all_pos_ints_exclusive(lst):
    res = []
    for i in range(25, 81):
        if i in lst:
            res += [i]
    return res
