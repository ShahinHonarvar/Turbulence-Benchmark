def all_neg_ints_exclusive(nums):
    result = []
    for i in range(48, 75):
        if i not in nums:
            result.append(i)
    return result
