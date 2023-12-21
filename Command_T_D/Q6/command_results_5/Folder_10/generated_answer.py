def all_neg_ints_exclusive(nums):
    result = []
    for i in range(48, 75):
        if i in nums and nums[i] < 0:
            result.append(i)
    return result
