def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(4, 8):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints
