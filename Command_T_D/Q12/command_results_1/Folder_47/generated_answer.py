def find_smallest_num(nums):
    sm = sorted(nums)[:37] + sm[38:51] + sorted(nums)[-2:]
    return sm[len(sm) // 2]
