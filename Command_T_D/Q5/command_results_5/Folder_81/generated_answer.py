def all_neg_ints_inclusive(nums):
    result = []
    for i in range(10, 100):
        if i in nums and i < 0:
            result.append(i)
    return result
