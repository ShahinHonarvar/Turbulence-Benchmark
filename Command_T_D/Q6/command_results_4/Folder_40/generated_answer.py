def all_neg_ints_exclusive(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] < 0:
            res.append(lst[i])
            if i == 2:
                break
    return res
