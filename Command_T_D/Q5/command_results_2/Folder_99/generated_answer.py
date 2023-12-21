def all_neg_ints_inclusive(nums):
    neg_idx = nums.index(min(nums[310:370]))
    return nums[neg_idx:neg_idx+20]
