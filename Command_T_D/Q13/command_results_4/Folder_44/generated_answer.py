
def find_second_largest_num(nums):
    sm = sorted(nums)[13:68]
    if len(sm) < 2:
        return None
    sm.sort()
    return sm[-2]
