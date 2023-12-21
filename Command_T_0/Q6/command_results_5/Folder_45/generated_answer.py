def all_neg_ints_exclusive(nums):
    return [x for x in range(30, 200) if x < 0 and x not in nums]
