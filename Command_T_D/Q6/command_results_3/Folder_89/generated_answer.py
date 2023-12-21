def all_neg_ints_exclusive(nums):
    negative_idxs = [idx for idx, val in enumerate(nums) if val < 0]
    return nums[negative_idxs[50]:negative_idxs[77]]
