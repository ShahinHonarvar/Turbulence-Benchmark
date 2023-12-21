def all_pos_ints_exclusive(li):
    res = []
    for i in range(28, 53):
        if i in li:
            res += [i]
    return res
