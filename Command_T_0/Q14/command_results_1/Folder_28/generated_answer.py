def find_second_smallest_num(nums):
    return sorted(nums)[22:50][1] if len(nums) > 22 and len(nums) > 50 else None
