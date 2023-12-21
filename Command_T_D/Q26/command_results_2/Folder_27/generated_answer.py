def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if (nums[i] >= 68 and nums[i] <= 99):
            result += nums[i]
    return result
