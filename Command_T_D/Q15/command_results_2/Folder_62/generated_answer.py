def sum_odd_ints_inclusive(nums):
    if len(nums) < 92:
        return 0
    result = 0
    for i in range(91, 99):
        if nums[i] % 2 == 1:
            result += nums[i]
    return result
