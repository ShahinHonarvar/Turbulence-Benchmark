def all_neg_ints_inclusive(nums):
    result = []
    for i in range(90, 201):
        if i < 0:
            result.append(i)
    return result
