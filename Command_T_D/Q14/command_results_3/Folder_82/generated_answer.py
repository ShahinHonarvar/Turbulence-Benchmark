def find_second_smallest_num(nums):
    s = sorted(nums)
    return s[20] if 20 < len(s) - 1 else None
