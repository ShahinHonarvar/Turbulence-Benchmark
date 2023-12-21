def all_neg_ints_exclusive(nums):
    res = []
    for i in range(0, len(nums) - 1):
        if nums[i] < 0:
            res.append(nums[i])
    return res
