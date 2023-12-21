def all_neg_ints_inclusive(nums):
    negs = []
    for i in range(40, 80):
        if i < 0:
            break
        elif nums[i] < 0:
            negs.append(i)
    return negs
