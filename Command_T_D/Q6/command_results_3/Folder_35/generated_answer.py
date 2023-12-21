def all_neg_ints_exclusive(nums):
    return [i for i in range(10, 80) if i < 0 and i not in nums]
