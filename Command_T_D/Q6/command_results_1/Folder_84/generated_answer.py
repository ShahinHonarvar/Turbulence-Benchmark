def all_neg_ints_exclusive(nums):
    negative_ints = [x for x in range(50, 93) if x < 0]
    return negative_ints if negative_ints else []
