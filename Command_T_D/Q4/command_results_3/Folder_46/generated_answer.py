def all_pos_ints_exclusive(nums):
    res = []
    for i in range(20, 43):
        if i in nums:
            res += [i]
    return res
