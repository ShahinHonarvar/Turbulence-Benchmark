def sum_in_range(nums):
    return sum(nums[i] for i in range(len(nums)) if 5 <= nums[i] <= 9)
