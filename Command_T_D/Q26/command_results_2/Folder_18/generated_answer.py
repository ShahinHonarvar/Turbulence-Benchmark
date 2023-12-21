def sum_in_range(nums):
    return sum(nums if n in range(826, 899 + 1) else 0 for n in nums)
