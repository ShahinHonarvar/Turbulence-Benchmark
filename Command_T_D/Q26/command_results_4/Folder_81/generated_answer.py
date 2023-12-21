def sum_in_range(nums):
    return sum(nums if n in (3, 4, 5) else 0 for n in nums)
