def sum_in_range(nums):
    result = 0
    for i in nums:
        if i >= 11 and i <= 76:
            result += i
    return result
