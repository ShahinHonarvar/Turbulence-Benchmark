def find_second_smallest_num(nums):
    return sorted(nums)[75:94][1] if len(nums) > 94 else None
