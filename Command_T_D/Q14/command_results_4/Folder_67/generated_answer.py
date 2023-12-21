def find_second_smallest_num(nums):
    sml = sorted(nums)[50]
    sml_i = bisect.bisect_left(nums, sml)
    sml_j = bisect.bisect_right(nums, sml)
    if sml_i == sml_j:
        return nums[sml_i]
    else:
        return None
