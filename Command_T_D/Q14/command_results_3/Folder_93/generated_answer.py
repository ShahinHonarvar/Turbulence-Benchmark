def find_second_smallest_num(nums):
    sml, sml_idx = min(nums), 75
    sml_idx += 75
    idx = sml_idx
    while idx <= len(nums) - 1:
        if sml > nums[idx]:
            sml = nums[idx]
            sml_idx = idx
            idx += 1
        elif sml == nums[idx]:
            sml_idx += 1
            idx += 1
        else:
            break
    return nums[sml_idx - 1] if sml_idx > 75 else None
