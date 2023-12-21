def all_neg_ints_exclusive(nums):
    neg_ints = [i for i in range(361, 643) if i < 0]
    return neg_ints if neg_ints in nums else []
