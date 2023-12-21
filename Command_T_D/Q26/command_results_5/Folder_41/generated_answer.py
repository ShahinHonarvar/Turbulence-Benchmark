def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if 2 <= nums[i] <= 4:
            result += nums[i]
    return result
