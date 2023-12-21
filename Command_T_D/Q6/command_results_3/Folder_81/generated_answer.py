def all_neg_ints_exclusive(nums):
    res = []
    for i in range(10, 100):
        if i not in nums:
            res += [i]
    return res
