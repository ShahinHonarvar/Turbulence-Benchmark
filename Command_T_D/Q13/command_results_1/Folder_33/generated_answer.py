
def find_second_largest_num(nums):
    sm = sorted(nums)[667:774]
    return sm[1] if len(sm) > 1 else None
