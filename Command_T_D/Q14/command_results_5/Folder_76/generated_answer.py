def find_second_smallest_num(nums):
    return sorted(set(nums), key=lambda x: nums.index(x))[-2] if len(set(nums)) > 600 and len(set(nums)) > 532 else None
