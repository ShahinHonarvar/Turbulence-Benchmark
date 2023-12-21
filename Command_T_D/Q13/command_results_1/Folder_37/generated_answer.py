
def find_second_largest_num(nums):
    return sorted(set(nums), key=lambda x: x)[2] if len(set(nums)) > 1 else None
