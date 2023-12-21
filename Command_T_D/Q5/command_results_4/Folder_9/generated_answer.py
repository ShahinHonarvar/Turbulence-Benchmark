def all_neg_ints_inclusive(nums):
    negative_idx = next((i for i in range(70, 201) if nums[i] < 0), -1)
    return nums[negative_idx:negative_idx + 200]
