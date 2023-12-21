def sum_in_range(nums):
    return sum(nums if (72 <= x <= 93) else [] for x in nums)
