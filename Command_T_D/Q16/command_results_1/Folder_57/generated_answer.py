def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(27, 55):
        if i % 2 == 0:
            result += nums[i]
    return result
