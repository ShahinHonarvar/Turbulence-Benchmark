def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(1, len(nums) + 1):
        if nums[i - 1] % 2 == 1:
            result += nums[i - 1]
    return result
