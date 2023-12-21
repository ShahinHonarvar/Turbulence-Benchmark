def all_neg_ints_exclusive(nums):
    neg_idx = nums.index(min(nums))
    return nums[neg_idx:neg_idx + 2]
