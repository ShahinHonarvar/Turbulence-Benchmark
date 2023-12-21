def all_neg_ints_inclusive(nums):
    result = []
    for i in range(21, 97):
        if i < 0:
            result.append(i)
    return result
