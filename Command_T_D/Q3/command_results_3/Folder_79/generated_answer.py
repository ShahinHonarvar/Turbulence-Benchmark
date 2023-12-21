def all_pos_ints_inclusive(nums):
    return [x for x in range(4, 4 + len(nums)) if x in nums and x > 0]
