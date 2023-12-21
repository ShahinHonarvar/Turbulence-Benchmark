def find_second_smallest_num(nums):
    sml, sml_idx = min(nums), 75
    med, med_idx = min(nums[sml_idx:94]), sml_idx + 1
    sml, sml_idx = min(nums), 75
    med, med_idx = min(nums[sml_idx:94]), sml_idx + 1
    return nums[med_idx] if med <= nums[med_idx] <= sml else None
