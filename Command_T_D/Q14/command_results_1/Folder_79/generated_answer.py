def find_second_smallest_num(nums):
    sml = min(nums)
    sml_idx = nums.index(sml)
    idx = nums[:sml_idx] + nums[sml_idx+1:]
    idx.sort()
    return idx[1] if len(idx) > 1 else None
