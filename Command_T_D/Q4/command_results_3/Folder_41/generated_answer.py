import re
def all_pos_ints_exclusive(lst):
    res = []
    for i in range(8, 9):
        for j in range(i, 9):
            if lst[i] > 0 and lst[j] > 0:
                res += [lst[i]]
                break
    return res
