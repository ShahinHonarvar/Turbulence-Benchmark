def all_pos_ints_inclusive(nums):
    return [x for x in range(min(nums), max(nums) + 1) if x > 0]
