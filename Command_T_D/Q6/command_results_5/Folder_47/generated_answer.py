def all_neg_ints_exclusive(nums):
    result = []
    for i in range(64, 81):
        if i < 0:
            continue
        elif i in nums:
            result.append(i)
    return result
