def all_neg_ints_inclusive(nums):
    result = []
    for i in range(62, 99):
        if i in nums and nums[i] < 0:
            result.append(i)
    return result
