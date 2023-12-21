def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    if not (nums[74] % 2 == nums[95] % 2):
        return []
    return nums[74:95] + [nums[95]]
