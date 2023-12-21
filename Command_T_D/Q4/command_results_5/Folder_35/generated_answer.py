def all_pos_ints_exclusive(lst):
    res = []
    for i in range(10, 79):
        if i in lst:
            res.append(i)
    return res
