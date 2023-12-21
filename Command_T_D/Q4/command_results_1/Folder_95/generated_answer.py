def all_pos_ints_exclusive(lst):
    res = []
    for i in range(25, 80):
        if lst[i] > 0:
            res.append(lst[i])
    return res
