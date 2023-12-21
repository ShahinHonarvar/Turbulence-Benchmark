def sum_odd_ints_inclusive(nums):
    result = 0
    for i in range(21, 98, 2):
        if i in nums:
            result += i
    return result
