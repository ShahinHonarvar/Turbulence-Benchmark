 
def all_ints_div_by_num(lst):
    res = []
    for i in range(12, 93):
        if lst[i] % -14 == 0:
            res.append(lst[i])
    return res
