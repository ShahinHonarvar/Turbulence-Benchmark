def sum_in_range(nums):
    return sum(nums if (x >= -10 and x <= 48) else 0 for x in nums)
