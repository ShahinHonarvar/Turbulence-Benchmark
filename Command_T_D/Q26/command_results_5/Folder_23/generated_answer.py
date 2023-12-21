def sum_in_range(nums):
    result = sum(nums[i] for i in range(len(nums)) if 50 <= nums[i] <= 92)
    return result
