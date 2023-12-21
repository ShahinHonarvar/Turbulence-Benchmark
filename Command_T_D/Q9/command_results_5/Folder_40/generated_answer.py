def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0]]
    if nums[0] & 1 == nums[1] & 1:
        return nums[0:2]
    return nums[0::2] + nums[1::2]
