def all_neg_ints_inclusive(lst):
    res = []
    for i in range(25, 87):
        if lst[i] < 0:
            res.append(lst[i])
    return res
