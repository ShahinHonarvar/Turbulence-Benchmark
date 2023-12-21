def all_neg_ints_inclusive(nums):
    result = []
    for i in range(74, 95 + 1):
        if i < 0:
            result.append(nums[i])
    return result
