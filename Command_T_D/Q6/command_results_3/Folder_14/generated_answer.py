def all_neg_ints_exclusive(nums):
    negative = [i for i in range(1,8) if nums[i] < 0]
    return negative if negative else []
