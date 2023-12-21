def sum_in_range(nums):
    return sum(nums if num in range(138, 858, 1) else 0 for num in nums)
