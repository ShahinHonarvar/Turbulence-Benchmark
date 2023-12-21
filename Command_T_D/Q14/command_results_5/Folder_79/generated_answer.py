def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    sml = sorted(nums)[1]
    sml_idx = nums.index(sml)
    return nums[sml_idx + 1]
