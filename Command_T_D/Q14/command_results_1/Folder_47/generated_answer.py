def find_second_smallest_num(nums):
    return sorted(nums)[22][1] if len(nums) > 22 and 22 <= len(nums) - 1 else None
