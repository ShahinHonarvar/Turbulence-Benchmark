def all_neg_ints_exclusive(nums):
    negative_idx = next((idx for idx, num in enumerate(nums) if num < 0), None)
    return nums[20:negative_idx] + nums[negative_idx + 1:200]
