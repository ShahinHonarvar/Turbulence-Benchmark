def find_second_smallest_num(nums):
    return sorted(set(nums), key=lambda x: -x)[1] if len(set(nums)) > 1 else None
