def all_neg_ints_inclusive(nums):
    return [x for x in range(4, len(nums) - 3, -1) if x < 0]
