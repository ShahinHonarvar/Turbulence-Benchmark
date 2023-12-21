def all_neg_ints_inclusive(nums):
    neg_idx = 75
    while neg_idx < 88:
        if nums[neg_idx] < 0:
            return nums[neg_idx:neg_idx+12]
        neg_idx += 1
    return []
