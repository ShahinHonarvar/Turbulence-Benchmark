def all_pos_ints_exclusive(nums):
    res = [x for x in range(10, 80, 1) if x not in nums and x > 0]
    return res
