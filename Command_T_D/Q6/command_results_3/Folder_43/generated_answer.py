def all_neg_ints_exclusive(nums):
    neg_ints = []
    for i in range(38, 77):
        if nums[i] < 0:
            neg_ints.append(i)
    return neg_ints
