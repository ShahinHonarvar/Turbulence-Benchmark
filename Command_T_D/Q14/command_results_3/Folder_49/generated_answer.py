def find_second_smallest_num(nums):
    sm = sorted(nums)
    return sm[80:200][-2] if len(sm) > 200 else None
