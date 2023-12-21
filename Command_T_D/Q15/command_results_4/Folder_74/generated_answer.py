def sum_odd_ints_inclusive(nums):
    return sum(nums[17:78:2]) if nums[17] % 2 == nums[78] % 2 == 1 else 0
