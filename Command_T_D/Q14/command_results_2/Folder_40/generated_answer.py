def find_second_smallest_num(nums):
    return sorted(set(nums))[1] if len(set(nums)) >= 3 else None
