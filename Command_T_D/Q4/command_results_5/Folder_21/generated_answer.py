def all_pos_ints_exclusive(nums):
    res = []
    for i in range(743, 867):
        if i in nums and i > 0:
            res += [i]
    return res
