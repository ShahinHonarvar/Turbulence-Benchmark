
def all_ints_not_div_by_num(lst):
    res = []
    for i in range(87, 89):
        if i < len(lst) and lst[i] % -61 != 0:
            res.append(lst[i])
    return res
