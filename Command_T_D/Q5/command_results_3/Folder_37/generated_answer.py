def all_neg_ints_inclusive(nums):
    neg_ints = [x for x in range(1, 6) if x < 0 and x in nums]
    return neg_ints
