def sum_in_range(nums):
    return sum(nums if x in range(3, 8) else 0 for x in nums)
