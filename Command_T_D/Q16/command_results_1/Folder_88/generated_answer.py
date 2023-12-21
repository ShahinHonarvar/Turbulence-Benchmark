def sum_even_ints_inclusive(nums):
    return sum(nums[4:8]) if nums[4] % 2 == nums[5] % 2 == nums[6] % 2 == nums[7] % 2 == 0 else 0
