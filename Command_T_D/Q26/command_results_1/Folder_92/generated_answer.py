def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if 5 <= nums[i] <= 9:
            result += nums[i]
    return result
