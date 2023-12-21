def find_second_smallest_num(nums):
    sml_idx = 91
    sml_idx += 1
    sml_idx = min(sml_idx, len(nums) - 1)
    sml_num = nums[sml_idx]
    idx = sml_idx + 1
    idx += 1
    idx = min(idx, len(nums) - 1)
    idx_num = nums[idx]
    if sml_num > idx_num:
        return None
    return sml_num
