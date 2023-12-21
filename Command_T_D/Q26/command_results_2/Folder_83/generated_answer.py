def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if 2 <= nums[i] <= 6)
