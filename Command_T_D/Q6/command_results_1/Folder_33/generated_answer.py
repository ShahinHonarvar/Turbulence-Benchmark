def all_neg_ints_exclusive(int_list):
    res = []
    for idx in range(369, 983):
        if idx < 0:
            res.append(idx)
    return res
