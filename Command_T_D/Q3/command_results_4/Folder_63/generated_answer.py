def all_pos_ints_inclusive(lst):
    res = []
    for i in range(22, 88 + 1):
        if i in lst:
            res.append(i)
    return res
