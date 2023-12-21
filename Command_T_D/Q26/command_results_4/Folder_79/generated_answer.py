def sum_in_range(nums):
    result = 0
    for n in nums:
        if 2 <= n <= 9:
            result += n
    return result
