def all_pos_ints_inclusive(lst):
    res = []
    for i in range(30, 87):
        if i in lst:
            res += [i]
    return res
