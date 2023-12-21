def all_pos_ints_exclusive(nums):
    res = []
    for i in range(2, len(nums) + 1):
        if i > 0 and nums[i - 1] > 0:
            res += [nums[i - 1]]
        if i < len(nums) and nums[i] > 0:
            res += [nums[i]]
    return res
