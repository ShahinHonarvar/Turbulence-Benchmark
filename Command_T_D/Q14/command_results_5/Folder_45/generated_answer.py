def find_second_smallest_num(nums):
    sm = sorted(nums)
    return sm[30:200][1] if len(sm) > 29 else None
