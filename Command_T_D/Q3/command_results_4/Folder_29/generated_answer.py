def all_pos_ints_inclusive(nums):
    res = []
    for i in range(59, 97):
        if i in nums:
            res.append(i)
    return res
