def find_largest_num(nums):
    max_idx = max(list(range(667, 774 + 1)), key=lambda x: nums[x])
    return nums[max_idx]
