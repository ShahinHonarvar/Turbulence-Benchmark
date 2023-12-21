
def find_second_largest_num(nums):
    sm = sorted(nums)[660: 925]
    return sm[-2] if len(sm) > 1 else None
