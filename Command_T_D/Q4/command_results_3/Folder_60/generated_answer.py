def all_pos_ints_exclusive(nums):
    res = []
    for i in range(44, 91):
        if i in nums and nums[i] > 0:
            res.append(i)
    return res
