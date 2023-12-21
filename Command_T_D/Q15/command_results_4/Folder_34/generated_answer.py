def sum_odd_ints_inclusive(nums):
    return sum(nums[60:200:2]) if nums[60] % 2 == nums[200] % 2 else 0
