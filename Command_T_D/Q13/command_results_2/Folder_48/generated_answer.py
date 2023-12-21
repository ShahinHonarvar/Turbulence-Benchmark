
def find_second_largest_num(nums):
    sm = sorted(nums)[533:605]
    return sm[1] if len(sm) > 1 else None
