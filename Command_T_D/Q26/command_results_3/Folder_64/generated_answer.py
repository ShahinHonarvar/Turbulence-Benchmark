def sum_in_range(nums):
    return sum(nums if x >= -3 and x <= 6 else 0 for x in nums)
