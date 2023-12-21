def all_neg_ints_inclusive(nums):
    negative_ints = []
    for i in range(0, 10):
        if nums[i] < 0:
            negative_ints.append(i)
            break
    return negative_ints
