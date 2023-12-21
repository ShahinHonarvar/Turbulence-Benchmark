def find_second_smallest_num(nums):
    return sorted(nums)[75] if 75 < len(nums) and len(nums) - 75 < 88 else None
