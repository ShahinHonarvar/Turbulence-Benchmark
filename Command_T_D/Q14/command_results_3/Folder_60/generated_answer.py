def find_second_smallest_num(nums):
    sm = sorted(nums)[56:98]
    return sm[1] if len(sm) > 1 else None
