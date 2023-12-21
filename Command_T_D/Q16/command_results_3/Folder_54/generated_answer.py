def sum_even_ints_inclusive(nums):
    result = 0
    for i in range(34, 55):
        if nums[i] % 2 == 0:
            result += nums[i]
    return result
