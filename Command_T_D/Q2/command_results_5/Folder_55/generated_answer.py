def all_ints_exclusive(nums):
    result = nums[:10]
    result.extend(nums[11:])
    return result
