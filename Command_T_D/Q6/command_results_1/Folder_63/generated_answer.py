def all_neg_ints_exclusive(nums):
    negative_idxs = [i for i, x in enumerate(nums) if x < 0]
    if len(negative_idxs) == 0:
        return []
    return nums[negative_idxs[0]:negative_idxs[-1]] + nums[:negative_idxs[0]] + nums[negative_idxs[-1]:]
