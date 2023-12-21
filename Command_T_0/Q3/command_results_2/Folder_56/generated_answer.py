def all_pos_ints_inclusive(nums):
    return [x for x in range(0, len(nums)) if x >= 0 and x < len(nums) and nums[x] > 0]
