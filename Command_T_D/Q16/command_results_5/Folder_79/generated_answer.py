def sum_even_ints_inclusive(nums):
    return sum(nums[4:-4] if len(nums) > 4 else [])
