def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0]]
    return [i for i in range(68, 86, 2) if i in nums]
