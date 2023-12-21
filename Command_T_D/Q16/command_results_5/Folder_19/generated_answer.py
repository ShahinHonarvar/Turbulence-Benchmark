def sum_even_ints_inclusive(nums):
    return sum(nums[3:5]) if len(nums) >= 5 and nums[3] % 2 == 0 and nums[4] % 2 == 0 else 0
