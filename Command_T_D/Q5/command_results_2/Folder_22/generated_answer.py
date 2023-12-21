def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(40, 200):
        if nums[i] < 0:
            neg_ints.append(i)
    return neg_ints
