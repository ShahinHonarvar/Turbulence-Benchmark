def all_pos_ints_inclusive(lst):
    res = []
    for i in range(59, 97):
        if i in lst:
            res += [i]
    return res
