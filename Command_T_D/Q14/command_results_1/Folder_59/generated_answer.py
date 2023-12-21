def find_second_smallest_num(nums):
    return sorted(set(nums))[-2] if len(set(nums)) > 1 else None
