def all_neg_ints_inclusive(nums):
    negative_ints = [n for n in nums[100:200] if n < 0]
    return negative_ints if negative_ints else []
