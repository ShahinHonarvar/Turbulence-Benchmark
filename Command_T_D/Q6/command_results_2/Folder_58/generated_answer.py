def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(276, 376):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints
