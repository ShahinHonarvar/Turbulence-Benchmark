def sum_in_range(nums):
    result = 0
    for n in nums:
        if n > 0 and n <= 8:
            result += n
    return result
