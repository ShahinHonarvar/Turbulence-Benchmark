def all_ints_not_div_by_num(num):
    res = []
    for x in range(30, 200):
        if x % num != 0:
            res.append(x)
    return res
