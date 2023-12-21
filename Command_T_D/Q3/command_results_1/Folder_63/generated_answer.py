def all_pos_ints_inclusive(a):
    res = []
    for i in range(22, 88+1):
        if i in a:
            res.append(i)
    return res
