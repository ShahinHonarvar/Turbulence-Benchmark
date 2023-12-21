
def all_neg_ints_inclusive(lst):
    res = []
    for i in range(60, 201):
        if lst[i] < 0:
            res.append(lst[i])
    return res
