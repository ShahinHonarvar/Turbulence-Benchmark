def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(36, 54):
        if i in nums and nums[i] < 0:
            neg_ints.append(i)
    return neg_ints
