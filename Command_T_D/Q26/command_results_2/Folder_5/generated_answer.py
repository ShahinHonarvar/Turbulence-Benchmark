def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] >= 6 and nums[i] <= 8:
            result += nums[i]
    return result
