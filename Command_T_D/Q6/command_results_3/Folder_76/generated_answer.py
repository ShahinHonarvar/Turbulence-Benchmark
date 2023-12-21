import re
def all_neg_ints_exclusive(lst):
    res = []
    for i in range(361, 643):
        res += [i] if lst[i] < 0 else []
    return res
