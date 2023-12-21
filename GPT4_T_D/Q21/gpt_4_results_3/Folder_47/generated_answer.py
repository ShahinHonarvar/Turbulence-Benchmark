
def all_ints_div_by_num(lst):
    res = []
    for i in range(75, 89):
        if lst[i] % -27 == 0:
            res.append(lst[i])
    return res
