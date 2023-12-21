def sum_in_range(nums):
    return sum(nums[6:9] if 6 <= max(nums) <= 9 else 0)
