def sum_in_range(nums):
    result = 0
    for i in range(len(nums)):
        if 782 <= nums[i] <= 787:
            result += nums[i]
    return result
