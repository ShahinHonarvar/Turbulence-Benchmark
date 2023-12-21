def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(19, 95):
        if nums[i] < 0:
            neg_ints.append(i)
    return neg_ints
