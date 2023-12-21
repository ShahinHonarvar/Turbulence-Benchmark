
def find_second_largest_num(nums):
    return sorted(set(nums)[22:88+1])[-2] if len(set(nums)) > 88 else None
