def all_neg_ints_exclusive(nums):
    res = []
    for i in range(20, 43):
        if nums[i] < 0:
            res.append(nums[i])
    return res
