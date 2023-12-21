def all_neg_ints_inclusive(nums):
    result = []
    for i in range(6, 8):
        if i in nums and nums[i] < 0:
            result.append(nums[i])
    return result
