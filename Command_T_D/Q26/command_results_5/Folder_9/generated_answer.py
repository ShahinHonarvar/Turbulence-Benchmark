def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if nums[i] in range(4, 6))
