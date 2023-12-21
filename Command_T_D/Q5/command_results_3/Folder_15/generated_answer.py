def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(len(nums) - 1):
        if nums[i] < 0:
            neg_ints.append(nums[i])
            break
    return neg_ints
