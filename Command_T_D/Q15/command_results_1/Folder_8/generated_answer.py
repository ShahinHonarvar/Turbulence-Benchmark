def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(23, len(nums), 2):
        result += nums[i]
    return result
