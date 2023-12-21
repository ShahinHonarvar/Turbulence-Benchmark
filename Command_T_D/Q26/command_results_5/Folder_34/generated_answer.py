def sum_in_range(nums):
    result = sum(x for x in nums if x >= 4 and x <= 7)
    return result if result else 0
