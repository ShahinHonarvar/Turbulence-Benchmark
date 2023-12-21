def all_pos_ints_inclusive(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] > 0:
            res += [lst[i]]
    return res
