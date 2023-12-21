def all_pos_ints_inclusive(nums):
    return [x for x in range(len(nums)) if x >= 0 and x < len(nums) and isinstance(nums[x], int) and nums[x] > 0]
