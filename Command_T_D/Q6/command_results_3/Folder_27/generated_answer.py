def all_neg_ints_exclusive(nums):
    negative_ints = [int(i) for i in range(28, 49) if str(i) in str(nums) and str(i) in str(nums)[::-1]]
    return negative_ints
