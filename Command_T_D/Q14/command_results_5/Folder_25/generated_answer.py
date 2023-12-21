def find_second_smallest_num(nums):
    sm = sorted(nums)
    return sm[37] if len(sm) > 38 else None
