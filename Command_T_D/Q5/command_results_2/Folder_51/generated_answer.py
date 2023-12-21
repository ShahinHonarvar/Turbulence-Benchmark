def all_neg_ints_inclusive(nums):
    return [i for i in range(1, 9) if i * i <= min(nums) and i * i <= max(nums) and nums[i] < 0]
