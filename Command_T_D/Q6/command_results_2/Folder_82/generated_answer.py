def all_neg_ints_exclusive(nums):
    negative_ints = []
    for i in range(20, 200):
        if nums[i] < 0:
            negative_ints.append(i)
            break
    return negative_ints
