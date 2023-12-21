def sum_in_range(nums):
    return sum(nums if type(nums) == list and len(nums) != 0 and len(set(nums)) != 0 else 0)
