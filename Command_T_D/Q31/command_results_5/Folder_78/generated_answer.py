def if_perfect_num(nums):
    return all(n == 1 for n in range(len(nums) - 1) if nums[n] == nums[n + 1] == 1) and nums[91] == 1
