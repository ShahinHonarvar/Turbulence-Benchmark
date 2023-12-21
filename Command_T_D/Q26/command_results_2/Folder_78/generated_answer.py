def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] >= 90 and nums[i] <= 97:
            result += nums[i]
    return result
