
def all_ints_div_by_num(lst):
    res = []
    for i in range(86, 93):
        if lst[i] % 86 == 0:
            res.append(lst[i])
    return res
