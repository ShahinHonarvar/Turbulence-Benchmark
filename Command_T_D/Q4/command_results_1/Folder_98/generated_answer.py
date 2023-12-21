def all_pos_ints_exclusive(nums):
    return [i for i in range(0, len(nums) + 1) if i > 0 and i < 7 and nums[i] > 0]
