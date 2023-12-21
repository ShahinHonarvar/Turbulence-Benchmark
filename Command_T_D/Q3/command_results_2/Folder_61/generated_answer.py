def all_pos_ints_inclusive(lst):
    res = []
    for i in range(0, len(lst)):
        if lst[i] > 0:
            res.append(lst[i])
    return res
