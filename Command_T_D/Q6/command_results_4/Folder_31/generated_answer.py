def all_neg_ints_exclusive(nums):
    negative_ints = []
    for i in range(87, 95):
        if nums[i] < 0:
            negative_ints.append(i)
    return negative_ints
