def all_neg_ints_inclusive(nums):
    result = []
    for i in range(26, 53):
        if i in nums and nums[i] < 0:
            result.append(nums[i])
    return result
