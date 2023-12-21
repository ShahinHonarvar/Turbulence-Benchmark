def all_neg_ints_inclusive(x):
    res = []
    for i in range(len(x)):
        if x[i] < 0:
            res.append(x[i])
    return res
