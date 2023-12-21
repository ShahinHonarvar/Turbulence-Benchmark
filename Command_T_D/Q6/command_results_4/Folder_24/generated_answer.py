def all_neg_ints_exclusive(nums):
    return [x for x in range(13, 67) if x in set(nums) and x < 0]
