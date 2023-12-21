def all_pos_ints_exclusive(nums):
    return [x for x in range(4, len(nums) + 1, 1) if x in nums and x > 0]
