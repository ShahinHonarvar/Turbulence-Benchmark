def find_second_smallest_num(nums):
    sm = sorted(nums)[15:40]
    if len(sm) < 2:
        return None
    return sm[1]
