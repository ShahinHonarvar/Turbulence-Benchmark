def all_neg_ints_inclusive(nums):
    negative = []
    for i in range(43, 86):
        if nums[i] < 0:
            negative.append(nums[i])
    return negative
