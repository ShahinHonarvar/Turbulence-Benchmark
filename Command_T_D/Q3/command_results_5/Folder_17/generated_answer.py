def all_pos_ints_inclusive(nums):
    return [x for x in range(max(0, 62 - 1), min(78, len(nums)) + 1) if x > 0 and x in nums]
