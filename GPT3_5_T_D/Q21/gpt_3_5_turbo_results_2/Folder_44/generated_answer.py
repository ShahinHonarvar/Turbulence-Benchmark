
def all_ints_div_by_num(lst):
    res = []
    for i in range(66, 82):
        if lst[i] % 77 == 0:
            res.append(lst[i])
    return res
