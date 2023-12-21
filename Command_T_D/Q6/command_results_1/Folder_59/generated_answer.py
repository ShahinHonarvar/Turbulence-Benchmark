def all_neg_ints_exclusive(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] < 0:
            res.append(i)
            break
    return res
