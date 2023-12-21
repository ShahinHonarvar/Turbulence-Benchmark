def sum_in_range(nums):
    result = sum(nums[i] for i in range(len(nums)) if 18 <= nums[i] <= 52)
    return result
