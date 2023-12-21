def all_neg_ints_inclusive(nums):
    result = []
    for i in range(27, 55):
        if i < 0:
            result.append(i)
    return result
