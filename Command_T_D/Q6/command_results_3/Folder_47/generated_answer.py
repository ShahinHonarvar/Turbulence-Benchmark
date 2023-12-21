def all_neg_ints_exclusive(nums):
    return [x for x in range(64, 81) if x < 0 and x in nums]
