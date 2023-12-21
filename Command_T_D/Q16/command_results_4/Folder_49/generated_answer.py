def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(8, min(len(nums), 80), 2):
        result += nums[i]
    return result
