def all_neg_ints_exclusive(num_list):
    res = []
    for i in range(len(num_list)):
        if num_list[i] < 0:
            res.append(num_list[i])
    return res
