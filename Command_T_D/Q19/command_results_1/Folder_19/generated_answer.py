import re
def all_ints_not_div_by_num(lst):
    idx = -1
    while idx < 4:
        if lst[idx] % -7 != 0:
            break
        idx += 1
    idx = -1
    while idx < 5:
        if lst[idx] % -7 != 0:
            break
        idx += 1
    return lst[idx-1:idx+1]
