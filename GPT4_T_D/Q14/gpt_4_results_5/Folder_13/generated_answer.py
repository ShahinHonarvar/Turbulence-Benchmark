
def find_second_smallest_num(nums):
    if len(nums)<33:
        return None
    else:
        limited_list = sorted(nums[28:33])
        return limited_list[1] if len(limited_list) > 1 else None
