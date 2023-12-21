def all_pos_ints_inclusive(nums):
    return [i for i in range(0, len(nums) + 1) if i >= 0 and i <= 5 and isinstance(nums[i], int) and nums[i] > 0]
