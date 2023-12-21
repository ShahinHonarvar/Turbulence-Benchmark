def sum_in_range(nums):
    result = 0
    for n in nums:
        if n >= 3 and n <= 7:
            result += n
    return result
