
def all_ints_not_div_by_num(lst):
    res = []
    for i in range(39, 52):
        if lst[i] % -41 != 0:
            res.append(lst[i])
    return res
