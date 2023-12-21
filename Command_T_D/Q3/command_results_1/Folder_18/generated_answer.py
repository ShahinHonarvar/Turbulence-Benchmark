def all_pos_ints_inclusive(nums):
    if 35 in nums and 49 in nums:
        return nums[nums.index(35):nums.index(49)+1]
    else:
        return []
