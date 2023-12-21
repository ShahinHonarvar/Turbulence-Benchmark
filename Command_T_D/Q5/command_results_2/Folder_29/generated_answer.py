def all_neg_ints_inclusive(nums):
    negative_ints = [i for i in range(59, 97) if nums[i] < 0]
    return negative_ints
