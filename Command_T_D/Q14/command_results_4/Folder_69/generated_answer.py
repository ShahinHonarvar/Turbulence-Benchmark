def find_second_smallest_num(nums):
    sm = sorted(nums)[:25] + sm[25:-87] + sm[87:]
    return sm[1] if len(sm) > 1 else None
