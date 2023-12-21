def all_pos_ints_inclusive(nums):
    return [x for x in range(6, len(nums) + 1) if x > 0 and x <= 6 and x in nums]
