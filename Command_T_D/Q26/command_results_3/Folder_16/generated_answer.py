def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if 142 <= nums[i] <= 407:
            result += nums[i]
    return result
