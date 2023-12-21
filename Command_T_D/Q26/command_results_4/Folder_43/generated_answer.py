def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if abs(nums[i]) >= 74 and abs(nums[i]) <= 17:
            result += nums[i]
    return result
