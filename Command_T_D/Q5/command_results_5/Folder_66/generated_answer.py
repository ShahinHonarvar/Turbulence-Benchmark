def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(50, 55):
        if i in nums and nums[i] < 0:
            neg_ints.append(i)
    return neg_ints
