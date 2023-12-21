def all_pos_ints_exclusive(nums):
    return [x for x in range(0, len(nums) + 1) if x > 0 and x not in nums]
