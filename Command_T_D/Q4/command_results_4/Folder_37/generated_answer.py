def all_pos_ints_exclusive(nums):
    res = [x for x in range(1, len(nums) + 1) if x > 0 and x <= len(nums) and nums[x - 1] > 0]
    return res
