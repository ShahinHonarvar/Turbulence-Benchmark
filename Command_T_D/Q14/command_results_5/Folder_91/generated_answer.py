def find_second_smallest_num(nums):
    sml = sorted(set(nums))[:5]
    return sml[1] if len(sml) > 1 else None
