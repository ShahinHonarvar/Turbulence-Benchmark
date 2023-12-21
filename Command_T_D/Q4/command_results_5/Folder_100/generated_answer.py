def all_pos_ints_exclusive(a):
    res = []
    for i in range(22, 25):
        if a[i] > 0:
            res += [a[i]]
    return res
