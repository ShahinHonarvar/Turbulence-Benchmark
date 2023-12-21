def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(63, 100):
        if i % 2 == 1:
            result += nums[i]
    return result
