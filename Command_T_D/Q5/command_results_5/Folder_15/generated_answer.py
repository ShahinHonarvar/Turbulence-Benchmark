def all_neg_ints_inclusive(nums):
    negative_ints = [x for x in nums if x < 0]
    return negative_ints[:4] if negative_ints else []
