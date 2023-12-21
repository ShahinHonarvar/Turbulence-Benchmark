
def find_second_largest_num(nums):
    return sorted(set(nums))[-2] if len(set(nums)) > 74 and len(set(nums)) > 95 else None
