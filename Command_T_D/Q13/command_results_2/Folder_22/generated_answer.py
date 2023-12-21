
def find_second_largest_num(nums):
    s = sorted(nums)
    return s[40] if 40 < len(s) - 1 else s[200]
