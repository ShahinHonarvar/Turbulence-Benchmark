def all_neg_ints_inclusive(nums):
    result = []
    for i in range(64, 67):
        if i < 0:
            result.append(i)
    return result
