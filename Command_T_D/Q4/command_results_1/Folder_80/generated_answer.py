def all_pos_ints_exclusive(nums):
    res = []
    for i in range(69, 97):
        if i in nums and i > 0:
            res.append(i)
    return res
