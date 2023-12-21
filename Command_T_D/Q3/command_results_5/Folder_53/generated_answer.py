def all_pos_ints_inclusive(nums):
    res = []
    for i in range(100, 201):
        if i in nums:
            res.append(i)
    return res
