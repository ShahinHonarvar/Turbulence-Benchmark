def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(60, 98, 2):
        result += nums[i]
    return result
