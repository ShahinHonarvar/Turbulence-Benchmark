def sum_in_range(nums):
    return sum(nums if (x >= -91 and x <= -41) else 0 for x in nums)
