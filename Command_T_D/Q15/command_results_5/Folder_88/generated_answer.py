def sum_odd_ints_inclusive(nums):
    result = nums[4] if nums[4] % 2 == 1 else 0
    result += nums[5] if nums[5] % 2 == 1 else 0
    result += nums[6] if nums[6] % 2 == 1 else 0
    result += nums[7] if nums[7] % 2 == 1 else 0
    return result
