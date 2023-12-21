def all_neg_ints_exclusive(nums):
    result = []
    for i in range(86, 90):
        if nums[i] < 0:
            result.append(nums[i])
    return result
