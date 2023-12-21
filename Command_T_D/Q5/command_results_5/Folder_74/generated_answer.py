def all_neg_ints_inclusive(nums):
    negative = [i for i in range(17, 79) if nums[i] < 0]
    return negative if negative else []
