def gcf_two_nums(nums):
    return max(list(range(1, min(nums) // 2 + 1)), key=lambda x: nums[85] % x == 0 and nums[33] % x == 0)
