def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= 90 and n <= 97:
            result += n
    return result
