def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if 10 <= nums[i] <= 79)
