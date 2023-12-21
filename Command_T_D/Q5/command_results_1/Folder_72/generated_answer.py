def all_neg_ints_inclusive(nums):
    result = [x for x in range(29, 51) if x in nums and x < 0]
    return result
