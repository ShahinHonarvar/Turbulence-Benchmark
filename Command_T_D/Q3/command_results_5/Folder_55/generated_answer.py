def all_pos_ints_inclusive(nums):
    return [i for i in range(0, len(nums) + 1) if i > 0 and i <= 10 and nums[i - 1] > 0]
