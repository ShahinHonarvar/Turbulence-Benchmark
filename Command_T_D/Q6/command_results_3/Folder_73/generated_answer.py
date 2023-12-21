def all_neg_ints_exclusive(num_list):
    res = []
    for i in range(36, 85):
        if num_list[i] < 0:
            res.append(num_list[i])
    return res
