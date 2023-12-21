def all_neg_ints_inclusive(nums):
    return [i for i in range(310, 370) if i in nums and nums[i] < 0]
