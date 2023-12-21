def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if abs(nums[i]) >= 798 and abs(nums[i]) <= 379:
            result += nums[i]
    return result
