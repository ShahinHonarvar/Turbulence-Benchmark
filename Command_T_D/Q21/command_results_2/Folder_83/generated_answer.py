def all_ints_div_by_num(lst):
    res = []
    for idx in range(40, 401):
        if idx % 7 == 0:
            res.append(lst[idx])
    return res
