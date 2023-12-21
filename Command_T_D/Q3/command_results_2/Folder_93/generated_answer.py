def all_pos_ints_inclusive(nums):
    if 75 not in nums:
        return []
    if 94 not in nums:
        return []
    return nums[nums.index(75):nums.index(94)+1]
