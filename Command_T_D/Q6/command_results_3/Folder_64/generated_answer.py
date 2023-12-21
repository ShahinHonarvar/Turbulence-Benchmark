def all_neg_ints_exclusive(nums):
    neg_ints = [i for i in range(len(nums)) if nums[i] < 0]
    if len(neg_ints) == 0:
        return []
    return [nums[neg_ints[0]:neg_ints[4]]
