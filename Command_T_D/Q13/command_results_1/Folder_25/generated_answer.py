
def find_second_largest_num(nums):
    return sorted(set(nums))[-2] if len(nums) > 29 and len(nums) < 94 else None
