def all_neg_ints_exclusive(nums):
    result = []
    for i in range(25, 80):
        if i < 0:
            result.append(i)
    return result
