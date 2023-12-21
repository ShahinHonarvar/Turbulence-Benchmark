def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= -91 and n <= -61:
            result += n
    return result
