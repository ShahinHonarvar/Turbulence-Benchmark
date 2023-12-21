def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(37, 77):
        if i % 2 == 0:
            result += nums[i]
    return result
