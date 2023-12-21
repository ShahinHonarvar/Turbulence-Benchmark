def find_second_smallest_num(nums):
    s = sorted(nums)
    return s[22:63][1] if 22 <= len(s) - 1 and len(s) - 1 <= 63 else None
