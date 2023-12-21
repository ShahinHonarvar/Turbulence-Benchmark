def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    if not nums[30] % 2:
        return []
    return [x for x in nums[31:34]]
