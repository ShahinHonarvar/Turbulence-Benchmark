def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= -64 and n <= 42:
            result += n
    return result
