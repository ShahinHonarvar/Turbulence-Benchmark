def sum_even_ints_inclusive(nums):
    return sum(nums[::2]) if len(nums) > 1 else 0
