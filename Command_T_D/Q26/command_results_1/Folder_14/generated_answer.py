def sum_in_range(nums):
    result = 0
    for i in nums:
        if i >= 3 and i <= 7:
            result += i
    return result
