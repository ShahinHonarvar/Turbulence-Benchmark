def find_second_largest_num(nums):
    return sorted(nums)[3] if len(nums) > 2 else None
