def all_neg_ints_inclusive(nums):
    return [x for x in range(1, len(nums)+1) if x in nums and nums[x] < 0]
