def find_second_smallest_num(nums):
    return sorted(nums)[5] if len(nums) > 4 else None
