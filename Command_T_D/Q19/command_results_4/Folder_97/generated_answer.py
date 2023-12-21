def all_ints_not_div_by_num(list_of_ints):
    res = []
    for i in range(14, 48):
        if not (i % 16):
            continue
        res.append(i)
    return res
