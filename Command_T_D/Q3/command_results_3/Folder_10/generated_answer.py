def all_pos_ints_inclusive(list):
    res = []
    for i in range(25, 60):
        if i in list:
            res.append(i)
    return res
