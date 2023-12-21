def find_second_smallest_num(nums):
    return sorted(nums)[10] if len(nums) > 9 else None
