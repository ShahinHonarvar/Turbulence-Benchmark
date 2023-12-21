def all_neg_ints_exclusive(lst):
    res = []
    for i in range(0, len(lst) - 1):
        if lst[i] < 0:
            res.append(lst[i])
    return res
