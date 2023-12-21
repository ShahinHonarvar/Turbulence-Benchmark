def all_neg_ints_inclusive(nums):
    return [x for x in range(len(nums)) if x >= 0 and x < 5 and nums[x] < 0]
