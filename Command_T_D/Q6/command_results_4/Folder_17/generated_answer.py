def all_neg_ints_exclusive(nums):
    return [x for x in range(len(nums)-2, -1, -1) if x < 0 and x not in nums]
