def all_pos_ints_exclusive(nums):
    return [i for i in range(32, 99, 1) if i in nums and nums[i] > 0]
