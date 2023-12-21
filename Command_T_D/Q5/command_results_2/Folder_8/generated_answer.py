def all_neg_ints_inclusive(nums):
    return [x for x in range(23, len(nums) - 1, -1) if x in nums and nums[x] < 0]
