def find_second_smallest_num(nums):
    return sorted(nums)[64] if len(nums) > 63 else None
