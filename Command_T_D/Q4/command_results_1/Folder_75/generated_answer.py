def all_pos_ints_exclusive(lst):
    res = []
    for i in range(20, 37):
        if lst[i] > 0:
            res.append(lst[i])
    return res
