def all_neg_ints_exclusive(nums):
    result = []
    for i in range(276, 376):
        if nums[i] < 0:
            result.append(nums[i])
    return result
