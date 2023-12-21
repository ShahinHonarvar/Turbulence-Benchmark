def all_neg_ints_inclusive(nums):
    negative_idx = 90
    while negative_idx < len(nums) - 1:
        if nums[negative_idx] < 0:
            break
        negative_idx += 1
    return nums[negative_idx:negative_idx + 100]
