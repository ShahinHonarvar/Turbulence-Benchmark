def all_neg_ints_exclusive(nums):
    result = []
    for i in range(81, 87):
        if i in nums and nums[i] < 0:
            result.append(nums[i])
    return result
