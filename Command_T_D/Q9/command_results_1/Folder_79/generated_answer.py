def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    if 4 not in nums:
        return []
    result = [num for num in nums[4:]]
    if 4 not in result:
        return []
    return result
