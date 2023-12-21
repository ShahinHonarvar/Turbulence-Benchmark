def all_neg_ints_inclusive(nums):
    return [x for x in range(len(nums)) if x in nums and x < 0]
