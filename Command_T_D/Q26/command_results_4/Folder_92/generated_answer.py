def sum_in_range(nums):
    return sum(nums if x in range(5, 10) else 0 for x in nums)
