def all_neg_ints_inclusive(nums):
    return [i for i in range(12, 92) if i in nums and nums[i] < 0]
