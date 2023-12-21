def all_pos_ints_exclusive(nums):
    res = [x for x in range(111, 473, 1) if x in nums]
    return res
