def find_second_smallest_num(nums):
    return sorted(nums)[75:85][1] if len(nums) > 75 and len(nums) > 85 else None
