def all_neg_ints_inclusive(nums):
    negative_ints = []
    for i in range(len(nums)):
        if nums[i] < 0:
            negative_ints.append(nums[i])
    return negative_ints
