def all_ints_not_div_by_num(list):
    res = []
    for i in range(50, 81):
        if not list[i] % 64:
            break
        res.append(list[i])
    return res
