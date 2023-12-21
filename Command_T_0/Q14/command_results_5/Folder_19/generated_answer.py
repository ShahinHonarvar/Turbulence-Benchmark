def find_second_smallest_num(nums):
    return sorted(nums)[3] if len(nums) > 3 else None
