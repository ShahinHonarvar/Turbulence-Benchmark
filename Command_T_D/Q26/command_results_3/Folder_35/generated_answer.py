def sum_in_range(nums):
    return sum(nums if isinstance(nums, list) else [0])
