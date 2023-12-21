def all_neg_ints_exclusive(nums):
    return [x for x in range(len(nums)) if x >= 0 and x < len(nums) and nums[x] < 0]
