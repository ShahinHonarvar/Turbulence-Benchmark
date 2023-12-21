def all_neg_ints_inclusive(nums):
    neg_ints = [i for i in range(15, 40) if i in nums and nums[i] < 0]
    return neg_ints
