def all_pos_ints_inclusive(nums):
    return [i for i in range(4, len(nums) + 1, 1) if isinstance(nums[i], int) and nums[i] > 0]
