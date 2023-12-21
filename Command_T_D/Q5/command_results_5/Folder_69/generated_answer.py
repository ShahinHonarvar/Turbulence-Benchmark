def all_neg_ints_inclusive(nums):
    negative_ints = []
    for i in range(32, 35):
        if nums[i] < 0:
            negative_ints.append(i)
    return negative_ints
