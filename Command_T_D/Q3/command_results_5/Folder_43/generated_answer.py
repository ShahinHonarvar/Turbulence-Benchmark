def all_pos_ints_inclusive(lst):
    res = []
    for i in range(68, 86 + 1):
        if lst[i] > 0:
            res += [lst[i]]
    return res
