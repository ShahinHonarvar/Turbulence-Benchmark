import re
def all_ints_not_div_by_num(lst):
    res = []
    for i in range(469, 566):
        if not lst[i].is_integer():
            continue
        if lst[i] % -692 != 0:
            res.append(lst[i])
    return res
