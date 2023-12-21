def all_neg_ints_exclusive(nums):
    negative = nums[10:-10]
    if negative:
        negative = negative[::-1]
    return negative
