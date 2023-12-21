def all_pos_ints_exclusive(nums):
    return [x for x in range(len(nums)) if x > 0 and x < 3 and nums[x] > 0]
