def find_second_smallest_num(nums):
    return sorted(nums)[3] if len(nums) > 2 else None
