def all_neg_ints_exclusive(nums):
    neg_ints = [x for x in range(64, 81) if x in set(nums) and x < 0]
    return neg_ints
