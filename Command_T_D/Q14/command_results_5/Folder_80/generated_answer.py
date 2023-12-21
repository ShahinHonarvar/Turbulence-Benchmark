def find_second_smallest_num(nums):
    sm = sorted(nums)
    return sm[30:87][1] if len(sm) > 30 and len(sm) > 87 else None
