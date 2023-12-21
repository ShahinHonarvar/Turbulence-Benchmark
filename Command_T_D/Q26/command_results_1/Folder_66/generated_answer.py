def sum_in_range(nums):
    return sum(nums if (28 <= x <= 96) else 0 for x in nums)
