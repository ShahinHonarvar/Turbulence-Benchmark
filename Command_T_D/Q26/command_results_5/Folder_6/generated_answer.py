def sum_in_range(nums):
    return sum(nums if n in range(335, 612) else 0 for n in nums)
