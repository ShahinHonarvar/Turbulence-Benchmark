def find_second_smallest_num(nums):
    if len(nums) < 65:
        return None
    sml = sorted(nums)[64]
    sml2 = sorted(nums)[65]
    sml_temp = nums[sml:sml2 + 1]
    if len(sml_temp) == 1:
        return None
    return min(sml_temp)
