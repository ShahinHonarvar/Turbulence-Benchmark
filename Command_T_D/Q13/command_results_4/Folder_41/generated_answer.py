
def find_second_largest_num(nums):
    return sorted(set(nums))[-2] if len(set(nums)) > 5 else None
