def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= -23 and n <= 64:
            result += n
    return result
