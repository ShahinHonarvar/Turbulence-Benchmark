def sum_in_range(nums):
    return sum(nums if n in range(56, 91) else 0 for n in nums)
