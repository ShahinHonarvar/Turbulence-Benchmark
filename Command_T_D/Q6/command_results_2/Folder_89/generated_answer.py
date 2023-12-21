def all_neg_ints_exclusive(nums):
    neg_idxs = range(len(nums)-1, -1, -1)
    return [nums[idx] for idx in neg_idxs if nums[idx] < 0]
