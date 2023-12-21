def all_neg_ints_inclusive(nums):
    negative = [x for x in range(59, 97) if x < 0]
    return negative if negative else []
