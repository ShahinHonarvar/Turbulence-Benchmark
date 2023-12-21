def all_pos_ints_exclusive(a):
    res = []
    for i in range(36, 85):
        if i in a:
            res.append(i)
    return res
