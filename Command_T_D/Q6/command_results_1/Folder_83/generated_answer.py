def all_neg_ints_exclusive(nums):
    neg_idxs = set(range(90, 200)) & {idx for idx in range(90, 200) if nums[idx] < 0}
    return [nums[idx] for idx in neg_idxs]
