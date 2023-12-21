def find_second_smallest_num(nums):
    sml = nums[:]
    sml.sort()
    return sml[55:83][1] if 55 < len(sml) - 1 else None
