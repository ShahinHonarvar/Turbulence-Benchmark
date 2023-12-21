def sum_even_ints_inclusive(nums):
    return sum(nums[10::2] if len(nums) > 10 else [])
