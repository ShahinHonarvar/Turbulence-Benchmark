
def all_ints_not_div_by_num(lst):
    res = []
    for i in lst[9:8:-1]:
        if i % -3 != 0:
            res.append(i)
    return res
