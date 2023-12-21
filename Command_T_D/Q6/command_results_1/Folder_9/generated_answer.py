def all_neg_ints_exclusive(lst):
    res = []
    for i in range(70, 200):
        if lst[i] < 0:
            res.append(lst[i])
    return res
