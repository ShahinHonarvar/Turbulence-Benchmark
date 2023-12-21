def sum_in_range(nums):
    result = 0
    for x in nums:
        if x >= -97 and x <= -48:
            result += x
    return result
