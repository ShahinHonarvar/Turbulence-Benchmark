def all_neg_ints_exclusive(nums):
    result = []
    for i in range(48, 76):
        if nums[i] < 0:
            result.append(i)
    return result
