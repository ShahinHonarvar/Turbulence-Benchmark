def all_pos_ints_exclusive(nums):
    res = []
    for i in range(20, 36):
        if i not in nums:
            res.append(i)
    return res
