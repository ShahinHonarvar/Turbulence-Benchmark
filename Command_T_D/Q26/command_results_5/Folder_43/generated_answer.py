def sum_in_range(nums):
    result = 0
    for x in nums:
        if abs(x) >= 74 and abs(x) <= 17:
            result += x
    return result
