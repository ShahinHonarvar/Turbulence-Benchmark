def all_neg_ints_inclusive(nums):
    neg_ints = []
    for i in range(len(nums) - 50, len(nums) - 1):
        if nums[i] < 0:
            neg_ints.append(nums[i])
    return neg_ints
