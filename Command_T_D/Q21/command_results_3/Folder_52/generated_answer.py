import re
def all_ints_div_by_num(lst):
    idx = 42
    idx_num = 46
    idx_stop = 97
    res = []
    while idx < idx_stop:
        idx += 1
        res.append(lst[idx-1])
    return res
