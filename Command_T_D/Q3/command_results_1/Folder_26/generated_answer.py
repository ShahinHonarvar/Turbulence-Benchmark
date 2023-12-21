def all_pos_ints_inclusive(li):
    res = []
    for i in range(62, 99):
        if li[i] > 0:
            res += [li[i]]
    return res
