def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(310, 370 + 1):
        if nums[i] % 2 == 1:
            result += nums[i]
    return result
