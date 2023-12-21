def all_pos_ints_exclusive(nums):
    return [x for x in range(19, 95, 1) if x not in nums and x > 0]
