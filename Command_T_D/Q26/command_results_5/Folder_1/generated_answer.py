def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= -97 and n <= -48:
            result += n
    return result
