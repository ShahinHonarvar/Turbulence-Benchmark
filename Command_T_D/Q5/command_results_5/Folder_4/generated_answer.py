def all_neg_ints_inclusive(nums):
    return [x for x in range(len(nums) + 1) if x > 12 and x < 93 and nums[x] < 0]
