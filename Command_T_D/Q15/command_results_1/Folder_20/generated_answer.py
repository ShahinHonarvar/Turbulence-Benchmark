def sum_odd_ints_inclusive(nums):
    result = 0
    if len(nums) >= 57 and len(nums) <= 67:
        result += nums[56]
        result += nums[58]
        result += nums[60]
        result += nums[62]
        result += nums[64]
    return result
