def all_ints_exclusive(nums):
    result = nums[50:-1]
    result.extend(nums[201:])
    return result
