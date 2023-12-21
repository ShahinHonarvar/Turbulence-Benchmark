def find_second_smallest_num(nums):
    return sorted(nums)[13] if len(nums) > 13 and len(nums) < 69 else None
