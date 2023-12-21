def all_pos_ints_inclusive(nums):
    return [i for i in range(1, min(len(nums) + 1, 5) + 1) if nums[i - 1] >= 0]
