def find_largest_num(nums):
    max_idx = max(12, len(nums) - 92)
    return max(nums[max_idx:], default=-1)
