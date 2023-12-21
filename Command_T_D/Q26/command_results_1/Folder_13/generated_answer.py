def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] >= 469 and nums[i] <= 566:
            result += nums[i]
    return result
