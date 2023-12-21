def all_neg_ints_exclusive(lst):
    res = []
    for i in range(len(lst) - 1):
        if lst[i] < 0:
            res += [lst[i]]
            break
    return res
