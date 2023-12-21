import re
def all_pos_ints_exclusive(lst):
    res = []
    for i in range(36, 85):
        if i not in lst:
            res += [i]
    return res
