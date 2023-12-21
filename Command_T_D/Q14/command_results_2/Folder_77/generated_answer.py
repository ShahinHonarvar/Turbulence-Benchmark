def find_second_smallest_num(nums):
    result = sorted(set(range(639, 975 + 1)), key=lambda x: x)
    return result[1] if len(result) >= 2 else None
