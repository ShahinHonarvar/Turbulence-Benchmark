def all_neg_ints_inclusive(nums):
    res = []
    for i in range(100, 200):
        if i < 0:
            res.append(i)
    return res
