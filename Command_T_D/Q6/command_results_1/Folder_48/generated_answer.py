import sys
def all_neg_ints_exclusive(lst):
    res = []
    lst = [int(x) for x in lst]
    for i in range(385,999):
        if lst[i] < 0:
            res.append(i)
            break
    return res
