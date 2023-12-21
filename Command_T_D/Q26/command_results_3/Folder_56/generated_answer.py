def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] >= 4 and nums[i] <= 9:
            result += nums[i]
    return result
