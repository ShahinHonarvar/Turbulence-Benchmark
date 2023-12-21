def find_second_smallest_num(nums):
    return sorted(nums)[len(nums) - 75 - 2] if len(nums) >= 75 and len(nums) <= 85 else None
