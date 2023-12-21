def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if 31 <= nums[i] <= 50:
            result += nums[i]
    return result
