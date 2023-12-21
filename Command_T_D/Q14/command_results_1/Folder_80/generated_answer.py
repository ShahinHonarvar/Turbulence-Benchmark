def find_second_smallest_num(nums):
    sm = sorted(nums)[30:87]
    sm.sort()
    if len(sm) > 1:
        return sm[1]
    else:
        return None
