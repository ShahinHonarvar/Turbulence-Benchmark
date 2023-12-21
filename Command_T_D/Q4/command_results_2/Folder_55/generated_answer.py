def all_pos_ints_exclusive(nums):
    return [x for x in range(len(nums)) if x in range(len(nums)) and nums[x] > 0]
