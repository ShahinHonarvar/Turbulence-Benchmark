def sum_in_range(nums):
    result = 0
    for i in nums:
        if i >= 60 and i <= 97:
            result += i
    return result
