def all_pos_ints_exclusive(lst):
    res = []
    for i in range(361, 643):
        if i in lst:
            res.append(i)
    return res
