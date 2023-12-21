def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if nums[i] >= 4 and nums[i] <= 8)
